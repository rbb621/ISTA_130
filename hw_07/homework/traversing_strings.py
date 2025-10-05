'''
Name: Ricky Berliant
Date: 10/16/2025
Section Leader: Sungjoon
Week 7: Traversing Strings
File: traversing_strings.py
'''



# Example words
word_01 = 'Spongebob SquarePants'
word_02 = 'One Piece'
word_03 = input("Enter a word: ")

# Word 01 
n = 1
for i in range(len(word_01)):
    print(word_01[i] * n)

# To make a space
print()    


# Word 02 
j = 0
while j < len(word_02):
    character = word_02[j]
    print(character)
    j += 1

# To make a space
print()

# Word 03 
k = 0
while k < len(word_03):
    print(word_03[k])
    k += 1
