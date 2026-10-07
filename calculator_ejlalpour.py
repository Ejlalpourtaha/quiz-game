frist_number = input("Please Enter The Frist Number => ")
Mathematical_operations = input("Please Enter The One Of Mathematical Operations (+ Or - Or * Or /) => ")
second_number = input("Please Enter The Second Number => ")

frist_number = int(frist_number)
second_number = int(second_number)

ascii_Mathematical_operations = ord(Mathematical_operations)

if ascii_Mathematical_operations == 43:
    print(frist_number + second_number)
elif ascii_Mathematical_operations == 45:
    print(frist_number - second_number)
elif ascii_Mathematical_operations == 42:
    print( frist_number * second_number)
elif ascii_Mathematical_operations == 47:
    print(frist_number / second_number)
again = "Y"
while again == "Y":
    again = input("""Do you want to continue?
    Yes = Y , No = N : """)
    if again == "Y":
        frist_number = input("Please Enter The Frist Number => ")
        Mathematical_operations = input("Please Enter The One Of Mathematical Operations (+ Or - Or * Or /) => ")
        second_number = input("Please Enter The Second Number => ")

        frist_number = int(frist_number)
        second_number = int(second_number)

        ascii_Mathematical_operations = ord(Mathematical_operations)

        if ascii_Mathematical_operations == 43:
            print(frist_number + second_number)
        elif ascii_Mathematical_operations == 45:
            print(frist_number - second_number)
        elif ascii_Mathematical_operations == 42:
            print( frist_number * second_number)
        elif ascii_Mathematical_operations == 47:
            print(frist_number / second_number)