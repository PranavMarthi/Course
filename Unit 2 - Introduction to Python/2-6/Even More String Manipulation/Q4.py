name = input("Enter your first name and last name separated by comma (Pranav-Marthi): ")

first_initial = name[0].capitalize()
last_name_index = name.find("-")
last_name = name[last_name_index+1:].upper()
full_form = first_initial.upper() + name[last_name_index+1].upper() + last_name
print(full_form)
