try:
    file_obj = open("test.txt", "w")
    file_text = file_obj.write("Text from code.")
    file_obj.close()
    print("Writing done")

except Exception as e:
    print("Exception raised")
    print("Exception: ", e)