name = input("Enter your full name: ")

last_name_index = name.find(" ") + 1
print(last_name_index)
last_name = (name[last_name_index:]).upper()

first_name = name[:last_name_index].capitalize()

print("%s, %s" % (last_name, first_name))
