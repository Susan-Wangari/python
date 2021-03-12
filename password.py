x = str(input('Please Enter username: '))

username = "kay"
password = "1234"

if x == username :
    y = str(input ('Enter password: '))
    if y == password :
        print(len(y)) #
        print(x.upper())
        print(y.replace('1', '2'))
    print(y)
    print(username[1:])
else:
    print("wrong username")


