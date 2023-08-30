readable = open("india.txt", "r")
content = readable.read()
print(content.lower().count("india"))
