while True:

#menu
    print('''
    Welcome to the calculator app
    created by: vgiamp10
    below there is the list of what you can do

    -To do an addition, select 1;
    -to do a subtraction, select 2;
    -to do a multiplication, select 3;
    -to do a division, select 4;
    -to do a exponential calculation, select 5
    -to exit, write ESC;
    ''')
    #+
    scelta = input("select the number:")
    if scelta == "1":
        print("you selected: addition")
        a = float (input("insert the first number -> "))
        b = float (input("insert the second number -> "))
        print("the result is: " + str(a + b))
        break
    #-
    elif scelta == "2":
        print("you selected: subtraction")
        a = float (input("insert the first number -> "))
        b = float (input("insert the second number -> "))
        print("the result is: " + str(a - b))
        break
    #*
    elif scelta == "3":
        print("you selected: multiplication")
        a = float (input("insert the first number -> "))
        b = float (input("insert the second number -> "))
        print("the result is: " + str(a * b))
        break
    #/
    elif scelta == "4":
        print("you selected: division")
        a = float (input("insert the first number -> "))
        b = float (input("insert the second number -> "))
        print("the result is: " + str(a / b))
        break
    #**
    elif scelta == "5":al
        print("you selected: exponential calculation")
        a = float (input("inserte the base -> "))
        b = float (input("insert the exponent -> "))
        print("the result is: " + str(a ** b))
        break
    #exit
    elif scelta == "ESC":
        print("im exiting...")
        break