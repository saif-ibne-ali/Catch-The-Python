fruits =['mango','banana','orange','pineapple']
print(fruits)
print(fruits[3].title())

fruits.append('grapes')
print(fruits)
fruits.insert(0,'Berry')
print(fruits)
fruits.pop()
print(fruits)
del fruits[3]
print(fruits)
fruits.pop(2)
print(fruits)
fruits.remove('mango')
print(fruits)

##organizing List
cars = ['bmw','audi','toyota', 'honda','maruti','tata']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))

#avoiding index error
# print(cars[6]) --out of range
print(cars[-2]) #backtrack
