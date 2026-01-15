with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
