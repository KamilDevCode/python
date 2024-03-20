#  String data type

#  literal assignment
name = 'Kamil'
surname = "Lewandowski"

# funkca sprawdzająca typ danych:
# print(type(name))
# # print (type(name) == name)
# print (type(name) == str)
# print(isinstance(name, str))

#  constructor function

# pizza = str('pepperoni')
# print(type(pizza))
# print (type(pizza) == name)
# print (type(pizza) == str)
# print(isinstance(pizza, str))


#  Concatenation
print(name + ' ' + surname)
fullName = name + ' ' + surname
 

fullName += '!'
print(fullName)

# casting a number to a string:

decade = str(1990)
print(type(decade))

statement = "I like music from: " + decade + "s"

print(statement)


#  multiple lines:

multiline = """
hey how are you?
                  i am fine
    really?
    
                            sure
"""

print(multiline)

#  escaping special characters

sentence = "Hello, my name is \"Kamil\" I\`m"
print(sentence)

#  string methods:

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(multiline.replace('really?', 'very well'))


print(len(name))

print('')

#  string index values: indexing starts from 0
print(name[0])  # first letter: K
print(name[1])  # second letter: a
print(name[-1]) # last letter: l
print(name[0:3]) # first 3 letters: Kam

print('')

#  methods return boolean values
print(name.startswith('K'))
print(name.endswith('l'))

#  boolean data type:
value = True
value = bool(value)

print('')

x = 0
value = bool(x)



print(value)
print('')
print('')
print('')

#  numeric data type:
#  integer

#  integer
number1 = 42
number2 = int(42)
number3 = int(3.14)
number4 = int('42')

print(type(number3))
print(number3)

print('')
print('')
print('')
price = 100
bestPrice = int(60)

print(type(price))
print(isinstance(price, int))


# float
number1 = 3.14
number3 = float(3.14)
number4 = float('42')

print(type(number3))
print(number3)

print('')
print('')
print('')


#  complex

x = 3 + 4j
y = -2j
z = complex(1, -5)

print(x, y, z)  # Wydrukuje: (3+4j) (-0-2j) (1-5j)


#  built-in functions for numbers
print(abs(-5))  # 5
print(pow(2, 4))  # 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 3
print(round(3.75))  # 4

import math

print(math.pi)
print(math.ceil(3.14))
print(math.floor(3.14))
