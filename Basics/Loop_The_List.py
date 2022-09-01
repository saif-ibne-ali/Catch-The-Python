fruits =['mango','banana','orange','pineapple']
for fruit in fruits:
    print(fruit +" is important for vitamine")
    print(fruit.title())
    print(fruit.upper())
print(fruit)

for value in range(1,5):
    print(value)
print(list(range(1,6)))

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

##min and max functions
number = [11,12,118,0.34,6]
print(min(number))
print(max(number))


##list comprehension
square = [n**2 for n in range(1,11)]
print(square)

##Slicing a list
colour = ['red','blue','green','cyan']
print(colour[0:2])
print(colour[:-3])

mix = colour[:]
print(mix)