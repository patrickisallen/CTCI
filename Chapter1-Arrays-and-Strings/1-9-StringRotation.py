def string_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    print(string1 + string1)
    return is_substring(string1 + string1, string2)

def is_substring(string, sub):
    return string.find(sub) != -1

def main():
    print("Question 1.9\nAssume you have a method isSubstring which checks if one word is a substring of another.\nGiven two string s1 and s2 write code to check if s23is a rotation of s1\n using only one call to isSubstring")
    s1 = "tabletop"
    s2 = "optablet"
    print(string_rotation(s1,s2))


if __name__== "__main__":
    main()