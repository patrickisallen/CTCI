#Code only works with python 2 due to slice index
#best way to make a balanced BST from a sorted array is to start from the middle
def min_height_bst(arr):
    if len(arr) == 0:
        return None
    
    middle = len(arr) / 2
    left = min_height_bst(arr[:middle])
    right = min_height_bst(arr[middle+1:])
    return BSTNode(arr[middle], left, right)
    

class BSTNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right

  def __str__(self):
    string = "(" + str(self.data)
    if self.left:  string += str(self.left)
    else:          string += "."
    if self.right: string += str(self.right)
    else:          string += "."
    return string + ")"

def main():
    print('4-2')
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = min_height_bst(sorted_array)
    print(bst)

if __name__== "__main__":
    main()