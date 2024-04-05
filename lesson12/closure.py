# closure is a function having access to the scope of its enclosing function(outer function,parent function), even after the enclosing function has returned.


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # Wydrukuje 8


def parent_func(person):
    coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins == 0:
            print(f"{person} has no more coins")
        else:
            print(f"{person} has {coins} coins left")
            
    return play_game


persons = ["Anna", "Bob", "Charlie"]
play_game_functions = [parent_func(person) for person in persons]

for play_game_function in play_game_functions:
    play_game_function()