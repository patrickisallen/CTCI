def palindrome_permutation(string):
    cleanString = string.replace(" ", "")
    counter = Counter()
    #strip spaces & count letters
    for letter in string.replace(" ", ""):
        counter[letter] += 1

    odd_count = 0
    for count in counter.values():
        #checks if value is odd, if it is up the count
        odd_count += count % 2 
        #only 1 odd count allowed
        if odd_count > 1:
            return False
    return True

class Counter(dict):
  def __missing__(self, key):
    return 0

def main():
    print("Question 1.4\nPalindrome Permutation - Given a string, write a function to check if it\nis a permutation of a palindrome. A palindrome is a word or prhase\nthat is the same forwards and backwards")
    print(palindrome_permutation("tact coa"))

if __name__== "__main__":
    import sys
    import collections
    main()
