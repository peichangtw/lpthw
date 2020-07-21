from sys import argv

script, filename = argv

text = open(filename)

print(f"test {filename}")
print(text.read())

file_again = input('> ')

txt_again = open(file_again)

print(f"test {file_again}")

print(txt_again.read())

text.close()
txt_again.close()