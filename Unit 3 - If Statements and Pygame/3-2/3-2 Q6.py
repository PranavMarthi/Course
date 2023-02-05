string = input("Enter a string: ")
field_length = input("Enter a field length: ")


def centre(string_input, field_length_string):
    difference = int(field_length_string) - len(string_input)
    space_on_side = int(difference / 2)

    print("." * space_on_side + string_input + "." * space_on_side)


centre(string, field_length)
