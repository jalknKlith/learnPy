name = [""] * 5
age = [0] * 5
greater = 0
lower = 99
opc = 0

while opc != 4:
    print("Pick up a choice")
    print("1. Put your data")
    print("2. Show the data")
    print("3. Print the report")
    print("4. EXIT")
    opc = int(input())

    if opc == 1:
        for i in range(5):
            name[i] = input("Put a name: ")
            age[i] = int(input("Put the age: "))
            while age[i] < 18:
                age[i] = int(input("Try again (should be greater than 18): "))

    elif opc == 2:
        for i in range(5):
            if age[i] > greater:
                greater = age[i]
                j = i

        print("The oldest is:", name[j], "with", greater, "years")

        for i in range(5):
            if age[i] < lower:
                lower = age[i]
                k = i

        print("The youngest is: ", name[k], "with", lower, "years")

        avg = sum(age) / len(age)
        print("The age's average is: ", avg)

    elif opc == 3:
        print("The data of the students is:")
        for i in range(5):
            print("Name:", name[i], "- Age:", age[i])

    elif opc == 4:
        print("ENDING PROGRAM, THANKS!")

    else:
        print("Wrong choice, please, pick up the right option.")

