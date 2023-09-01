fav_animals = ['fox', 'panda', 'lion', 'cat']
print (fav_animals)
print ("panda")
fav_animals.remove('lion')
print (fav_animals)


fav_animals.append("wolf")
print (fav_animals)
for fav_animal in fav_animals:
    print ("i love", fav_animal)


numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
for number in numbers:
    numbers_sum+= number
    print (numbers_sum)