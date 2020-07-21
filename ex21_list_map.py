def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

age = add(30, 5)
height = subtract(100,10)
weight = multiply(10, 10)
iq = divide(100,100)

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,3))))

print(what)