##associate a value with a key
fruits ={
    'name':'mango',
    'color':'green'
}
print(fruits['color'])

print(fruits['color'])
fruits['color'] = 'yellow'

fruits['taste'] = 'sweet'

print(fruits)

del fruits['taste']
print(fruits)

###looping through a dictionary
user_0 ={
    'username' : 'github',
    'first_name' :'aspire',
    'last_name' : 'thinkpad'
}

for k, v in user_0.items():
    print("\n\tKey " + k)
    print("\tValue " +v)
for name in sorted(user_0.keys()):
    print(name.title())
for value in user_0.values():
    print(value.title())
##Nested Dictionary
mango = {'color':'green','taste':'sweetish'}
apple = {'color':'red','taste':'sweetish'}
pineapple = {'color':'greenish','taste':'sweetish'}
fruit = [mango,apple,pineapple]
print(fruit)

for item in fruit[0:3]:
    if item['color']=='red':
        item['color']='red-greenish'
        item['taste']='sweet'
print(fruit)

##A dictionary in a Dictionary
flowers = {
    'rose':{
        'color':['red','green'],
        'popularity':'high'
    },
    'lilly':{
        'color':['white','pink'],
        'popularity':'low'
    }
}  
for k,v in flowers.items():
    print("\nName "+k)
    print("color :"+str(v['color']))
    print("popularity : "+str(v['popularity']))  