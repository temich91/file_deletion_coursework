import os
with open("test.png", "wb") as file:
    print(file.write(b""))

os.remove("test.png")
