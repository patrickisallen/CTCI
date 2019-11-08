def partition(head, val):
    less_than_head, less_than_tail = None, None
    greater_than_head, greater_than_tail = None, None

    node = head
    while node:
        if node.data < val:
            #If value has already been inserted to head
            if less_than_head:
                less_than_tail.next = node
                less_than_tail = node
            else:
                less_than_head = node
                less_than_tail = node
        else:
            if greater_than_head:
                greater_than_tail.next = node
                greater_than_tail = node
            else:
                greater_than_head = node
                greater_than_tail = node

        node = node.next

    less_than_tail.next = greater_than_head
    return less_than_head

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next 

def main():
    print("Question 2.4\n")
    head = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8, None)))))))
    head2 = partition(head,7)
    while head2:
        print(head2.data)
        head2 = head2.next

if __name__== "__main__":
    main()