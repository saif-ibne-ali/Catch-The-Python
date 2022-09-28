
def greet_users(name):
    """Passing the list to the function"""
    for i in name:
        msg = "Hello, " + i.title() + "!"
        print(msg)

username = ['Saiful', 'islam', 'biplob']
greet_users(username)

PendingItems = ['OnePlus 9R','Lenovo Thinkpad','Iphone X']
ShippedItems = []

while PendingItems:
    items = PendingItems.pop()
    print("item name : " + items)

    ShippedItems.append(items)
print('\nThe items have been shipped :')
for i in ShippedItems:
    print(i)
print(PendingItems)