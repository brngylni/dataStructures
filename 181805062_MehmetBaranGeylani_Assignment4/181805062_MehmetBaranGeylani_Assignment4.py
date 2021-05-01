# Importing the random library for use some built-in methods.
import random
# Defining the one of the necessary functions.
def create_anagram(string):
    # Creating a new string randomly from given by the user.
    anagram = random.sample(string, len(string))
    return anagram
def str2chr2int(string):
    # Defining a list
    chr2int = []
    # Converting the string that given by the user to char then integer.
    for i in range(0, len(string)):
        char = string[i]
        chr2int.append(char)
    return chr2int

def int2chr2str(integer):
    # Defining a list.
    char = []
    string = ""
    # Converting the given integer to a char then string.
    for i in range(0, len(integer)):
        char[i] = chr(integer[i])
        string = string.append(char[i])
    return string

def compare2str(string1, string2):
    # Creating a condition that controls the length of strings.If they aren't same, we dont need to look another conditions.
    if(len(string1) == len(string2)):
        # Converting strings to their integer versions.
        int1 = [str2chr2int(string1)]
        int2 = [str2chr2int(string2)]
        # Sorting the list of integers by using bubble sort algorithm.
        sortedint1 = [sort_buble(int1)]
        sortedint2 = [sort_buble(int2)]

        for i in range(0, len(string1)):
            # We have two sorted arrays in here.All components must be equal to each other.
            # Controlling either they are equal or not.
            if(sortedint1[i] != sortedint2[i]):
                result = "These words are not anagram!"
                return result
            else:
                result = "These words are anagram!"
                return result
    else:
        result = "These words are not anagrams!"
        return result

def sort_buble(list):
    # Sorting the given list by using bubble sort algorithm.
    for i in range(0, len(list)):
        for j in range(0, i):
            if(list[i] < list[j]):
                list[i] , list[j] = list[j], list[i]

# Introduction to user about program.
print("Enter 2 words for checking either they are anagram or not.\nEnter 1 word to create a random anagram.\n")
# Prompting user to enter words.
string1 = input("Enter the first string : ")
string2 = input("Enter the second string(Press enter if you won't enter a number.) : ")
# Controlling either second string null or not.
if(string2 == ""):
    # Creating anagrams by using create_anagram function if second string is null.
    word = create_anagram(string1)
    anagram = ""
    for i in range(0,len(word)):
        anagram += word[i]
    # Printing the created anagram.
    print("Here is the anagram : " , anagram)
else:
    # Comparing the strings that given by the user by using compare2str function then printing it.
    print(compare2str(string1, string2))
