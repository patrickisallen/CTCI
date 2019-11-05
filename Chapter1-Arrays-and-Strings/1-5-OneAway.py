
#Wrong solutions
def one_edit(string1, string2):

    #check if length difference is greater than 1

    len_diff = abs(len(string1) - len(string2))
    if len_diff > 1:
        return False

    counter = Counter()
    for letters in string1:
        counter[letters] += 1
    
    for letters in string2:
        counter[letters] -= 1

    extraCount = 0
    for val in counter.values():
        if val < 0:
            extraCount += 1

    if extraCount > 1:
        return False
    return True

#correct solution
def one_edit_replace(string1, string2):
    edited = False
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            if edited:
                return False
            edited = True
        return True

def one_edit_insert(string1, string2):
    edited = False
    i, j = 0, 0
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True    

def one_edit_alt(string1, string2):
    if len(string1) == len(string2):
        return one_edit_replace(string1, string2)
    if len(string1) + 1 == len(string2):
        return one_edit_insert(string1, string2)
    if len(string1) - 1 == len(string2):
        return one_edit_insert(string2, string1)
    return False    


class Counter(dict):
  def __missing__(self, key):
    return 0

def main():
    print("Question 1.5\n")
    print(one_edit_alt("pale", "ple"))

if __name__== "__main__":
    import sys
    import collections
    main()