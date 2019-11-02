#! python

#Using Array Style
def isUnique(string):
    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
    return True

def main():
    print ("Question 1.1\nIs Unique: Implement an alg. to determine if a string has all unique characters. \nWhat if you cannot use additional data structures?\n")
    #Test input(s): patrick, allen, Aab, 0, 1, %$^&, ppaa, abcdefg, " " 
    testInput = ["patrick", "allen", "Aab", "0", "%$^&", "ppaa", "abcdefg", " " ]
    print("Test input(s): patrick, allen, Aab, 0, 1, %$^&, ppaa, abcdefg, " "")
    for words in testInput:
        print(isUnique(words))

if __name__== "__main__":
    main()