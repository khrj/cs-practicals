string = input("Enter string: ")
print("Palindrome" if string == string[::-1] else "Not palindrome")