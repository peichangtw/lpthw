mystuff = []

mystuff.append('hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbe"]

while len(stuff) <= 10:
    next_one = more_stuff.pop
    print(f"adding {next_one}")
    stuff.append(next_one)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
#print(' '.join(stuff))
#print('*'.join(stuff)[3:5])