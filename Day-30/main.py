try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    raise ArithmeticError("This is an error that I made up.")
    file.close()
    print("file was closed.")




