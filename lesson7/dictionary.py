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


#  ----------Sets:-------------

# 
nums = {1,2,3}
# constructor function:
nums2 = set({4,5,6})
print(nums)
print(type(nums))
print(nums2)
print(type(nums2))
print(len(nums2))

# no duplicate allowed: duplicate are ignored

nums  = {1,1,3,4,4}
print(nums)


"""

In this case, when the set nums is created, duplicate values are removed. Both True and False are interpreted as boolean values, where False is equivalent to 0 and True is equivalent to 1. As a result, only one of them will be retained in the set because they are equal to each other.
"""
nums = {0, 1, True, "Kamil", 2,2,3, False, }

print(nums)


# check if value is in the set:
print(2 in nums) # true 

# adding number tinto the set:
nums.add(20)
print(nums)

nums2 = {10,20,30,40}
nums.update(nums2)
print(nums)

# update can be used with lists, tuples, sets and with dictionaries:

lst = [1,2,3]
nums.update(lst)
print(nums)

tup = (10,20,30)
nums.update(tup)
print(nums)

dct = {"a":1, "b":2}
nums.update(dct)
print(nums)

# merge two sets:

one = {1,2,3,4,5,6,7,8,9,10}
two ={11,1,2,11,12,13,14,15,16,17,18,19,20}

# The union() method in Python is used to create a new set that contains all the unique elements from two or more sets. It combines the elements of the sets without any duplicates.
newSet = one.union(two)

print(newSet)

#  keep only the elements that are present in both sets:

newSet = one.intersection(two)
print(newSet)   # print the intersection of two sets: {1,2}

# keep only duplicate elements:

one ={1,2,3}
two ={1,2,3, 4,5,1}

one.intersection_update(two)
print(one)

# keep everything except duplicates:
one.symmetric_difference_update(two)
print(one)
