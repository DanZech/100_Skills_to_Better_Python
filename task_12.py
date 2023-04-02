s = input("Enter a sentence: ")
d = {"UPPER CASE": 0, "LOWER CASE": 0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass

print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])


'''
This is a Python program that counts the number of uppercase and lowercase letters 
in a sentence entered by the user, and prints the results. 

The program uses a dictionary to keep track of the counts, 
and loops through each character in the sentence using a for loop. 

If the character is uppercase, it increments the count of uppercase letters in the dictionary, 
and if it is lowercase, it increments the count of lowercase letters. 

Finally, the program prints the counts of uppercase and lowercase letters.
'''
