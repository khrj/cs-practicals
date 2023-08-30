readable = open("read.txt", "r")
writeable = open("write.txt", "w")

print("run")
lines = readable.readlines()

for line in lines:
    if line.startswith("a") or line.startswith("m"):
        writeable.write(line)

writeable.flush()
