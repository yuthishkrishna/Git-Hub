test_settings = {'theme': 'light'}

def add_setting(test_settings, setting):
    dict_setting = {setting[0].lower(): setting[1].lower()}
    key = list(dict_setting.keys())[0]
    value = dict_setting[key]

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings.update(dict_setting)  # merge new setting
        return f"Setting '{key}' added with value '{value}' successfully!"

print(add_setting(test_settings, ('THEME', 'dark')))
print(add_setting(test_settings, ('volume', 'high')))
print(test_settings)


def update_setting(test_settings, update):
    key = update[0].lower()
    value = update[1].lower()

    if key in test_settings:
        test_settings[key] = value   
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

print(update_setting(test_settings, ('theme', 'dark')))
print(update_setting(test_settings, ('volume', 'high')))
print(test_settings)


def delete_setting(test_settings,delete):
    key=delete.lower()
    
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"

    else:
        return "Setting not found!"

print(delete_setting(test_settings, 'theme'))
print(test_settings)

def view_settings(test_settings):
    if not test_settings:
        return "No settings available."

    formatted_settings = ""

    # Use a deterministic ordering so output is predictable in tests
    for key in sorted(test_settings.keys()):
        value = test_settings[key]
        formatted_settings += f"{key.capitalize()}: {value}\n"

    return formatted_settings

print(view_settings(test_settings))
