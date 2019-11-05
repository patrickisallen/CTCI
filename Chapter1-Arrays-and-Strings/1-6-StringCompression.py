def string_compression(string):
    if len(string) == 0:
        return string
    
    currCount = 1
    currLetter = string[0]
    parts = []

    for letter in string[1:]:
        if currLetter == letter:
            currCount += 1
        else:
            parts.append(currLetter + str(currCount))
            currLetter = letter
            currCount = 1
    #append last count because it is not included if there are multiple            
    parts.append(currLetter + str(currCount))            
    compressed = "".join(parts)
    if len(compressed) < len(string):
        return compressed
    else:
        return string
    

    

class Counter(dict):
  def __missing__(self, key):
    return 0


def main():
    print("Question 1.6\n")
    print(string_compression("aabbccc"))

if __name__== "__main__":
    main()