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

