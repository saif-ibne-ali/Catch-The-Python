###Naming Variables###
#contains only letters,numbers,underscore
#case sensitive
#space not allowed
#dont use keyword
#should be short and descriptive

#String Variable
sms = "catch the python"
print(sms)
print("I am 'typing' now")

name = "saiful islam"
print(type(name))
print(name.title())
print(name.upper())
print(name.lower())

nick_name= "Biplob"
print(name +" "+nick_name)

#adding white space in string
print("\tpython\npython\n\tCPP")

#stripping Whitespace
New_Name = " Human OS "
print(New_Name)
print(New_Name.lstrip())
print(New_Name.rstrip())


###Numbers
#integer
print(2+3)
print(2-3)
print(2*3)
print(2**3)
print(3%2)
print(3/2)
print(3*2.5)

###Avoiding Type errors
age = 25
msg ="Shanto is " + str(age) + " years old"
print(msg)
