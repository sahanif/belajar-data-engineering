text = input()
dict = {}
#your code goes here
for char in text:
    dict[char] = text.count(char)
    
print(dict)