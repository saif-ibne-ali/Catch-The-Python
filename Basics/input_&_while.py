from cmd import PROMPT


weight = input("please inter your weight: ")
print("your weight is :"+weight)
print(type(weight)) ##input is string type by default
weight = int(weight)
print(type(weight))

##introducing while loops
message = ""
while message != 'quit':
    message = input(PROMPT)
    if message !='quit':
        print(message)
##using a flag

active = True
while active:
    message=input(PROMPT)
    if message == 'quit':
        active = False
    else:
        print(message)

## use break and continue
while True:
    message=input(PROMPT)
    if message == 'quit':
        break
    else:
        print(message)

message = ""
while message != 'quit':
    message = input(PROMPT)
    print(message)
    continue
