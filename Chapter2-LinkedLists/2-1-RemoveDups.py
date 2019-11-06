def remove_duplicates(head):
    curr_node = head

    values_in_list = {}
    values_in_list[curr_node.data] = True

    while curr_node.next is not None:
        if curr_node.next.data in values_in_list:
            curr_node.next = curr_node.next.next
        else:
            values_in_list[curr_node.next.data] = True
            curr_node = curr_node.next
    
    return head

def remove_duplicates2(head):
  node = head
  if node:
    values = {node.data: True}
    while node.next:
      if node.next.data in values:
        node.next = node.next.next
      else:
        values[node.next.data] = True
        node = node.next
  return head

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

def main():
    print("Question 2.1\n")
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))

    second_copy = head

    while second_copy is not None:
        print(second_copy.data)
        if second_copy.next is  None:
            break
        second_copy = second_copy.next

    print("New list:")

    remove_duplicates2(head)

    while head is not None:
        print(head.data)
        if head.next is  None:
            break
        head = head.next

if __name__== "__main__":
    main()