file_name = input("Enter your file name (e.g., example.py): ")
file_extension_index = file_name.find(".") + 1
file_extension = file_name[file_extension_index:]
print("." + file_extension)
