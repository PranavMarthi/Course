def replace(string, old, new):
    for i in range(len(string)):
        if old == string[i:i+len(old)]:
            string = string[:i] + new + string[i+len(old):]
    return string


print(replace("Dogs and cats and dogs and cats", "Dogs", "cats"))
