import sys
script = sys.argv

# encoding codec
input_encoding = 'utf-8'
# error type
error = 'strict'

def main(language_file, encoding, errors):
    # read only one line
    line = language_file.readline()
    #print(line)
    # if not the end of file
    if line:
        # print line context
        #print(line)
        print_line(line, encoding, errors)
        # return main function to process next line
        return main(language_file,encoding,errors)

def print_line(line, encoding, errors):
    # strip th line
    next_lang = line.strip()
    #print(next_lang)
    # convert the line with encoding == utf-8
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # convert the line with decode == utf-8
    cooked_string = raw_bytes.decode(encoding,errors = errors)
    # print encode sting, decode string
    print(raw_bytes, '<===>', cooked_string)

languages = open('languages.txt', encoding='utf-8')
main(languages, input_encoding, error)

def print_line_new(line, encoding, errors):
    next_lang = line.strip()
    print(next_lang)

