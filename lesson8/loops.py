#  while loop:

value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value +=1
    
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else: 
    print("value is now:", value)
    
    print(type(value))
    
# -------for loop:------ 
 
names = ["Kamil", "Andrzej", "Ala","Adam", "Jan"]
 
for name in names:
     print(name)
     
for letter in "Kamil":
    print(letter)
    
for name in names:
    if name == "Adam":
        break
    print(name)
    
for name in names:
    if name == "Adam":
        continue
    print(name)
    
    # generate a sequence of numbers. It generates a range of integers that can be iterated over.By default, range() starts from 0 and increments by 1 for each subsequent value. Additional arguments like start, stop, and step can be provided to customize the behavior of the generated sequence
    
for x in range(10):
    print(x)
    
for x in range(2,6):
    print(x)
    
    
for x in range(0, 100, 5):
    print(x)
else:
    print("Glad that\'s the end of the loop!")
    
actions = ["eats", "sleeps", "codes", "cooks", "dances"]

names = ["Kamil", "Andrzej", "Ala","Adam", "Jan"]

# for action, name in zip(actions, names):
#     print(name, "can", action)
    
# for name in names: 
#     for action in actions:
#         print(name, action)
        
for action in actions:
    for name in names:
        print(name, action)