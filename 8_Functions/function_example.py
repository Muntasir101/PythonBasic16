def is_even_odd():
    a = int(input("Enter a number: "))

    if a % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


is_even_odd()


def bigger_number():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if a > b:
        print(f"{a} is bigger than {b}")
    else:
        print(f"{b} is bigger than {a}")


bigger_number()