print("step-1")


def greet():
    print ("Hello! Welcome to python")

greet()

print("step-2")


def greet(name):
    print (f"Hello, {name}!")

greet("Karthik")


print("step-3")


def square(x):
    return x * x
    
result = square(5)
print(result)

print("step-4")


def add(a, b):
    return a + b
    
print(add(3, 4))

print("step-5")


def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Karthik")


print("step-6")


def profile(name, age):
    print(f"Name: {name}, Age: {age}")
    
profile(age=18, name="Karthik")

print("step-7")


def total(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
    
print(total(1,2,3,4))

def details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
        
details(name="Karthik", age=18, city="Bangalore")


print("step-8")

def outer():
    def inner():
        print("This is inner function")
    print("Outer starts")
    inner()
    print("Outer ends")
    
outer()


print("step-9")


square = lambda x: x * x
print(square(6))



fruits = ["apple", "banana", "mango"]
print(fruits[1])
fruits.append("orange")
print(fruits)














