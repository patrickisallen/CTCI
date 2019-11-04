#Short method
def urlify(string):
    output = string.strip().replace(" ", "%20") #remove extra spaces
    return output

#Long Method
def urlify_alt(string):
  # Convert string to list to prepare to be modified
  letters = list(string)
  i = len(letters) - 1
  j = i
  while letters[i] == " ":
    i -= 1
  while j != i:
    # Replace space with %20
    if letters[i] == " ":
      letters[j-2] = "%"
      letters[j-1] = "2"
      letters[j]   = "0"
      j -= 2
    # Copy the original character
    else:
      letters[j] = letters[i]
    i -= 1
    j -= 1
  return ''.join(letters)



def main():
    print("Question 1.3\nURLify replace all spaces with %20")
    inputString = "This input string    "
    print(inputString)
    inputString = urlify(inputString)
    print(inputString)

if __name__== "__main__":
    main()