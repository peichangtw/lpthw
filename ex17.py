from sys import argv
from os.path import exists

script = argv
from_file = 'sample.txt'
to_file = 'output.txt'

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

in_file.close()
out_file.close()
