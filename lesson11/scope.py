#  global scope: explain:
#  This variable can be used anywhere in the program and have access into local scope.
name = "Kamil"

def greeting(firstname):
    print(f"Hello, I am {name} from global scope.")
    # Anna
    print(firstname)
    
greeting("Anna")

#  local scope:
#  This variable is only available in the scope inside the function.

def favorite_color():
    color = "blue"
    print(f"My favourite color is {color}.")
  
    
favorite_color()

# NameError: name 'color' is not defined
# print(color)

def another():
    greeting(f'greeting from another function, Kamil')
    # we can call function in local scope another function (enclosing scope)
another()


