class Planet:
    def __init__(self,name,planet_type,star):
        if not isinstance(name, str):
            raise TypeError("name, planet type, and star must be strings")
        elif not isinstance(planet_type, str):
            raise TypeError("name, planet type, and star must be strings")
        elif not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        if len(name) == 0:
            raise ValueError("name, planet type, and star must be non-empty strings")
        elif len(planet_type) == 0:
            raise ValueError("name, planet type, and star must be non-empty strings")
        elif len(star) == 0:
            raise ValueError("name, planet type, and star must be non-empty strings")
        
        else:
            self.name=name
            self.planet_type=planet_type
            self.star=star
    

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

    def orbit(self):
        return f"{self.name} orbits around {self.star}."

print('''1.Acess your own planet
2.Acess predefined planet Kepler-22b
3.Acess predefined planet WASP-12b
4.Acess predefined planet Gliese 581c''')

user_input=int(input("Enter the number corresponding to the planet you want to access: "))
if user_input == 1:
    name=input("Enter the name of your planet: ")
    planet_type=input("Enter the type of your planet: ")
    star=input("Enter the name of the star your planet orbits: ")
    user_planet=Planet(name,planet_type,star)
    print(user_planet)
    print(user_planet.orbit())
elif user_input == 2:
    planet_1=Planet('Kepler-22b','Super-Earth','Kepler-22')
    print(planet_1)
    print(planet_1.orbit())
elif user_input == 3:
    planet_2=Planet('WASP-12b','Hot Jupiter',' WASP-12')
    print(planet_2)
    print(planet_2.orbit())
elif user_input == 4:
    planet_3=Planet('Gliese 581c','Super-Earth',' Gliese 581 ')
    print(planet_3)
    print(planet_3.orbit())
else:
    print("Invalid input. Please enter a number between 1 and 4.")