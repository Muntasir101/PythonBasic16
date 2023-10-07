try:
    file_obj = open("test.txt", "r")
    file_text = file_obj.read()

    print(file_text)

    file_obj.close()

except Exception as e:
    print("Exception raised")
    print("Exception: ", e)