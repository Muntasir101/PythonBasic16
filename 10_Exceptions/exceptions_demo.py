try:
    a = 10
    b = 0
    result = a / b  # raised exception
    print(result)

except Exception as error:
    print("Exception raised")
    print("Exception: ", error)

print("Hello world")
