#using dictionary
def loop_detection(head):
    node_list = {}
    node = head
    
    while node:
        if node in node_list:
            return node
        else:
            node_list[node] = True
            node = node.next
        return None

#uses fast and slow pointer
def loop_detection_alt(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast
    

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

def main():
    print("Question 2.8\n")
    head1 = Node(100,Node(200,Node(300)))
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    print(loop_detection_alt(head2))
    

if __name__== "__main__":
    main()