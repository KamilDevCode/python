users = [
    'Kamil',
    'Adam',
    'Jan'
]

data = [True, 44, "Kamil"]



# # lists are zero-indexed
print(users[0]) # prints 'Kamil'

# # check lasts element of list
print(users[-1]) # prints 'Jan'


# # checking position of element
print(users.index('Jan')) # prints 2

# # checking range of elements of list 

print(users[0:2]) # prints ['Kamil', 'Adam']

# # checking range of elements of list 

print(users[0:]) # prints ['Kamil', 'Adam', 'Jan']

# #  lists are mutable
users[0] = 'Jan'

print(users) # prints ['Jan', 'Adam', 'Jan']

print(users[1]) # prints 'Adam' 


# # check if 'Adam' is in the list
print("Adam" in users) # True because 'Adam' is in the list


print('Jan' not in users) # False beacause 'Jan' is in the list


# # checking length of list with len() function
print(len(users)) # prints 3

# # adding username to list of users at the end of the list
users.append('Eliza')

# # adding usersname to list of users at the beginning of the list
users += ['Darek']


users.extend(['Milena', "Ania"])

users.insert(0, 'Piotr')


users[1:3] = ["Bożena", "Jacek"]

# removing element from list
users.remove('Piotr')
 
print(users.pop(0))

# deleting element from list with specified index

del users[0]

# clearing list of users, but list itself exists

users.clear()

users[1:2] = ['kamil']
 
 
# making list of users in alphabetical order
users.sort()

users.sort(key = str.lower)
 
print(users)
 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# reversing list  in reverse order
nums.reverse()

nums.sort(reverse = True)

numscopy = nums.copy()

mynums = list(nums)

print(nums)
print(numscopy)
print(mynums)


print(type(nums))

# tuples are immutable  

# tuple with constructor:
mytuple = tuple(('David', "John", "Michael"))

print(type(mytuple))

# tuple without constructor:
mytuple = (0, 1, 2, "John", "Michael")

print(mytuple.count(1))
print(mytuple.index(2)) 