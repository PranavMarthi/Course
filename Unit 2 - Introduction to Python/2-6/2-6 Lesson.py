# Three types of strings in Python:

"Sorta Standard"

'you see this one a lot in Python'

"""This one is
for multiple lines"""

food = "Butter"
bug = "fly"
prettyBug = food + bug
print(prettyBug)

print("=" * 40)

school = "White Oaks Secondary School"
print(school[1])
print(school[0])  # positions start at zero
print(school[-1])  # can count from the end
print(school[-2])
print(school[0:3])  # positions are seen as between letters
print(school[2:])
print(school[6:10])

# will give error (Strings are immutable)
# school[2] = 'X'

print(len(school))

print(school.upper())
print(school.replace('i', 'x'))
print(school.find(' '))
print(school.find("Ma"))
print(school.count("s"))
