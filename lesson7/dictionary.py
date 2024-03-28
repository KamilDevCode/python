# #  dictionaries similar to javaScript objects

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# #  constructor function:

band2 = dict(vocals = "Plant", guitar = "Page")

print (band)
print (band2)
print(type(band))  
print(len(band))

# #  access items: 
# # log output: Plant, Page   
print(band["vocals"]) 
print(band.get("guitar")) 

# #  list all available keys:

print(band.keys())

# #  list all available values:

print(band.values())

# #  list of key/value pairs as tuples:

print(band.items())

# #  verify that a key exists in the dictionary:

print("vocals" in band)
print("drummer" in band)

# # change values in the dictionary:

band["vocals"] = "Coverdale"

band.update({"vocals": "Ozzy", "bass": "Geezer"})
print(band)

# #  remove items from the dictionary:

print(band.pop("vocals"))
band["drums"] = "Bonham"

print(band.popitem()) # remove  items from the dictionary

# #  delete items from the dictionary:

band["drums"] = "Bonham"
del band["drums"]
print('band to teraz:', band)


# del band2
# print(band)


#  copy dictionary:

# band2 = band # create a reference to the same dictionary in the memory 
# print("---------Band copy----")


# print("band nr 1: ", band)
# print("band nr 2: ", band2)

# band2["drums"] = "Paice"

# print("band to:", band)
# print("band 2 to:", band2)

band2["drums"] = "Paice"
band2 == band.copy()

print("---COPY---")

print("band:", band)
print("band2:", band2)

# dictionary constructor functions: dict()

band3 = dict(band)
print("band3 :", band3)

# nested dictionaries:

member1 = {
    "name": "Kamil",
    "instrument": "guitar"
}

member2 = {
    "name": "Adam",
    "instrument": "drums"
}

band = {
    # "members": [member1, member2],
    "member1": member1, "member2": member2
}

print(band["member1"]["name"])

# print("band4 to", band4)
# print(member1["name"][])


