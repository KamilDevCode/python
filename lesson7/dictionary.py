#  dictionaries similar to javaScript objects

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

#  constructor function:

band2 = dict(vocals = "Plant", guitar = "Page")

print (band)
print (band2)
print(type(band))  
print(len(band))

#  access items: 
# log output: Plant, Page   
print(band["vocals"]) 
print(band.get("guitar")) 

#  list all available keys:

print(band.keys())

#  list all available values:

print(band.values())

#  list of key/value pairs as tuples:

print(band.items())

#  verify that a key exists in the dictionary:

print("vocals" in band)
print("drummer" in band)

# change values in the dictionary:

band["vocals"] = "Coverdale"

band.update({"vocals": "Ozzy", "bass": "Geezer"})
print(band)

#  remove items from the dictionary:

print(band.pop("vocals"))
band["drums"] = "Bonham"

print(band.popitem())

#  delete items from the dictionary:

band["drums"] = "Bonham"
del band["drums"]
# print(band)


band2.clear()
print(band2)