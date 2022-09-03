from unicodedata import name


def journey():
    print("Dhaka")
journey()

def journey(location):
    print("You are in "+location)
journey("Denmark")
journey("Jajiratul Arab")
journey(location="Bangladesh")

def fruits(name,color="green"):
    print(name + " is "+ color +" color")
fruits('mango')
fruits(name='guava')
fruits('Apple','Pink')

def Name_formation(first_nmae,last_name):
    full_name = first_nmae +" "+last_name
    return full_name.title()
nmae = Name_formation('saiful','islam')
print(nmae)

def city(name,country):
    placement = {'name':name,'country':country}
    return placement

target = city('Dhaka','Bangladesh')
print(target)
