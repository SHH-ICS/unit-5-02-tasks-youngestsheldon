# Create a program that will accept a word and output the word one letter at a time in reverse.

str = input("Input: ")
str = str[::-1]
for i in range(len(str)): print(str[i])