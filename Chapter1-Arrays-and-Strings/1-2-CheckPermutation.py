
def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    s1 = {}
    for letter in string1:
        if letter in s1:
            s1[letter] += 1
        else:
            s1[letter] =  1
    
    for letter in string2:
        if letter in s1:
            if s1[letter] < 0:
                return False
            else:
                s1[letter] -= 1
        else:
            return False
    
    for key in s1:
        if s1[key] != 0:
            return False
    
    return True;        

#cleaner implementation
def is_permutation_alt(str1, str2):
    counter = Counter()
    for letter in str1:
        counter[letter] += 1

    for key in counter:
        print(key, counter[key])
        
    for letter in str2:
        if not letter in counter:
            return False
        counter[letter] -= 1
        if counter[letter] == 0:
            del counter[letter]
    return len(counter) == 0

#defines implementation when a key is missing in dict
class Counter(dict):
    def __missing__(self, key):
        return 0

def main():
    print("Question X.X\n")
    string1 = "abc"
    string2 = "bac"
    string3 = "abb"
    string4 = "abcd"
    print(is_permutation_alt("abc", string2))

if __name__== "__main__":
    main()