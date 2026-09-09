from flask import Flask, render_template, request, jsonify
import os, requests

app = Flask(__name__)

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
AIR_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

WEATHER_CODES = {
    0:"Clear sky", 1:"Mainly clear", 2:"Partly cloudy", 3:"Overcast",
    45:"Fog", 48:"Depositing rime fog", 51:"Light drizzle", 53:"Moderate drizzle",
    55:"Dense drizzle", 61:"Slight rain", 63:"Moderate rain", 65:"Heavy rain",
    71:"Slight snow", 73:"Moderate snow", 75:"Heavy snow", 80:"Rain showers",
    81:"Moderate rain showers", 82:"Violent rain showers", 95:"Thunderstorm",
    96:"Thunderstorm with slight hail", 99:"Thunderstorm with heavy hail"
}

def get_json(url, params):
    r = requests.get(url, params=params, timeout=12)
    r.raise_for_status()
    return r.json()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/dashboard")
def dashboard():
    try:
        lat = float(request.args["lat"])
        lon = float(request.args["lon"])

        weather = get_json(WEATHER_URL, {
            "latitude": lat, "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m,wind_gusts_10m",
            "hourly": "temperature_2m,precipitation_probability,weather_code",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "forecast_days": 7,
            "timezone": "auto"
        })

        air = get_json(AIR_URL, {
            "latitude": lat, "longitude": lon,
            "current": "us_aqi,pm2_5,pm10,ozone,nitrogen_dioxide,sulphur_dioxide",
            "hourly": "us_aqi,pm2_5,pm10",
            "forecast_days": 7,
            "timezone": "auto"
        })

        return jsonify({
            "weather": weather,
            "air": air,
            "weather_codes": WEATHER_CODES
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.post("/api/advisory")
def advisory():
    data = request.get_json(force=True)
    profile = data.get("profile", {})
    current = data.get("current", {})

    age = profile.get("age", "adult")
    condition = profile.get("condition", "none")
    occupation = profile.get("occupation", "indoor")
    temp = current.get("temperature")
    aqi = current.get("aqi")
    pm25 = current.get("pm25")
    weather = current.get("weather")

    # Safe fallback: works without an LLM key.
    risk = "low"
    if aqi is not None:
        if aqi >= 201: risk = "very high"
        elif aqi >= 151: risk = "high"
        elif aqi >= 101: risk = "elevated"
        elif aqi >= 51: risk = "moderate"

    tips = []
    if condition == "asthma" and (aqi is not None and aqi >= 51):
        tips.append("Because you selected asthma, consider reducing prolonged outdoor exposure when air quality is elevated.")
    if occupation == "outdoor_worker" and (aqi is not None and aqi >= 101):
        tips.append("Because your work is outdoors, take regular breaks in cleaner indoor air and follow your workplace safety guidance.")
    if temp is not None and temp >= 35:
        tips.append("It is hot enough to make outdoor activity more stressful, so stay hydrated and take breaks from heat.")
    if aqi is not None and aqi <= 50:
        tips.append("Air quality is currently in the good range.")
    if not tips:
        tips.append("Current conditions do not indicate a major weather or air-quality concern for the selected profile.")

    text = f"Personalized advisory: {risk.capitalize()} environmental risk right now. " + " ".join(tips)
    text += " This is general information, not medical advice."

    # Optional LLM enhancement if GROQ_API_KEY is configured.
    key = os.getenv("GROQ_API_KEY")
    if key:
        try:
            prompt = f"""Create a short plain-English environmental health advisory.
Do not diagnose, prescribe medication, or give emergency medical instructions.
Profile: age group={age}, health condition={condition}, occupation={occupation}.
Current conditions: temperature={temp} C, AQI={aqi}, PM2.5={pm25} ug/m3, weather={weather}.
Explain the practical difference this profile makes. Keep it to 3-5 sentences."""
            resp = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"model":"llama-3.1-8b-instant",
                      "messages":[{"role":"user","content":prompt}],
                      "temperature":0.2},
                timeout=15
            )
            resp.raise_for_status()
            text = resp.json()["choices"][0]["message"]["content"].strip()
            text += " This is general information, not medical advice."
        except Exception:
            pass

    return jsonify({"advisory": text, "risk": risk})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)