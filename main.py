word = input("Enter your text: ")
letter = input("Enter the letter, the number of which you want to cound: ")
result = 0

print("Your latter: ", letter)

for i in word:
    if i == letter:
        result += 1
print("The number of your latter: ", result)