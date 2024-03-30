def say_Hello(name, surname, age):
    return f'Hello, my name is {name} {surname} and I am {age} years old'
  
greeting = say_Hello('Kamil', 'Lewandowski', 33)

def sum(num1=0, num2=8):
    if(type(num1) is not int or type(num2) is not int):
        # print('Only integers are allowed') 
        return
    return num1 + num2
    
total = sum(2)
print(greeting)
print(total)

def multiple_items(items):
    result = 1
    for item in items:
        result *= item
    return result

result = multiple_items([1, 2, 3, 4, 5])
print(result)

def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items('Kamil', 'Adam', 'Jan')   