# Define a string
formatter = "{} {} {} {}"

# passing value to the func 
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

line = (
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)
# repr is representation 
print(">>>> line ", repr(line))

# passing multiple list, tuple
print(formatter.format(*line))