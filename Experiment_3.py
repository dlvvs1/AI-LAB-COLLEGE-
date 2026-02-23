import os
# --------- File Creation and Writing ---------
file = open("sample.txt", "w")
file.write("This is a sample file.\n")
file.write("Python file handling example.\n")
file.close()
# --------- File Reading ---------
file = open("sample.txt", "r")
print("File Contents:")
print(file.read())
file.close()
# --------- File Appending ---------
file = open("sample.txt", "a")
file.write("This line is appended to the file.\n")
file.close()
# --------- Reading After Appending ---------
file = open("sample.txt", "r")
print("Updated File Contents:")
print(file.read())
file.close()
# --------- File Deletion ---------
# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
#     print("File deleted successfully")
# else:
#     print("File does not exist")