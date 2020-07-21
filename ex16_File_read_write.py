from sys import argv

script = argv
filename = 'sample.txt'

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input('> ')

print('open the file')
#file object
target = open(filename, 'w')

print('Truncating the file, goodbye')
#Truncate == empty the file
target.truncate()

line1 = input('line1 >')
line2 = input('line2 >')
line3 = input("line 3: ")

print(f"I'm going to write these to the file.{filename}")

print(f'{line1}\n{line2}\n{line3}\n')
#write, writelines
# target.writelines(line1)
# target.write("\n")
# target.writelines(line2)
# target.write("\n")
# target.writelines(line3)
# target.write("\n")


#close the file
target.close()
