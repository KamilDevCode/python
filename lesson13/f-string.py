person = 'John'
coins = 4

# older way of formatting 
message = "\n%s has %d coins left" % (person, coins)

print(message)

message = "\n%s has %s coins left." %(person, coins)

print(message)

# new way of formatting:
message = f"{person} has {coins} coins left"

print(message)

message = "\n{1} has {0} coins left".format(person, coins)

print(message)

message = "\n{1} has {0} coins left".format(coins, person)

print(message)

message = "\n{person} has {coins} coins left".format(coins = coins, person=person)



player = {'person': 'Kamil', 'coins': 3}

print('last message:', message)
message = "\n{person} has {coins} coins left".format(
    **player)

print('last message:', message)

##########################################
# f-Strings:
message = f"\n{person} has {coins} coins left"
print(message)

message = f"\n{person} has {3 * 5} coins left"
print(message)

# we can use a method:
message = f"\n{person.upper()} has {3 * 5} coins left"
print(message)

message = f"\n{player['person']} has {3 * 5} coins left"
print(message)

# formatting options:
num = 10
print(f"\n2.25 times {num}  is {2.25 * num:.2f}.\n")

for num in range(1,11):
    print(f"2.25 times {num}  is {2.25 * num:.2f}.")

for num in range(1,11):
    print(f"{num}  divided by 4.52 is  {num / 4.52:.2%}.")