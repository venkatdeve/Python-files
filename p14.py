import os
print(os.getcwd())

print(os.listdir())
print(os.path.exists("p1.py"))
print(os.path.isfile("p1.py"))
print(os.path.isdir("p13.py"))
print(os.name)

if os.name == "posix":
    print("This is posix os , means Unix type")
    os.system("ls -ltr")
elif os.name == "nt":
    print("This is windows os ")
    os.system("dir")
else:
    print("Unsupported OS")