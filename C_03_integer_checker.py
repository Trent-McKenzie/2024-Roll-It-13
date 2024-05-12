while True:

    error = "Please enter an integer that is 13 or more."

    try:
        my_num = int(input("Enter an integer: "))

        if my_num < 13:
            print(error)
            
        print("Your number is ", my_num)

    except ValueError:
        print(error)
