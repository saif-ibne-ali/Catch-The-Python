available_items = ['Rice','Carry','Fish','Fruit','Meat']

age = 12
if age <4:
    print('Your admit fee is $0.')
elif age <18:
    print('Your admit fee is $10.')
elif age <14:
    print('Your admit fee is $5.')
if age <15:
    print('Admission not availabe')
## if conditions check every line but elif stop checking if a condition is true.

requested_items = ['salad','Rice','Carry','Meat']

for items in requested_items:
    if items in available_items:
        print('The item is available ' + items)
    else:
        print("sorry! we don't have "+items)