def is_palindrome(head):
    node = head
    stack = []

    while node:
        stack.append(node.data)
        node = node.next

    while head and len(stack):
        if head.data != stack.pop():
            return False
        head = head.next
    
    return True

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

def main():
    print("Question 2.6\n")
    list1 =  Node("b",Node("o",Node("b")))
    list2 = Node(4,Node(9,Node(5)))
    list3 = Node(4,Node(9,Node(5, Node(5, Node(9, Node(4))))))


    print(is_palindrome(list3))
    

if __name__== "__main__":
    main()