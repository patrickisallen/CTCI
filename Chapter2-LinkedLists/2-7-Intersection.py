def intersection(l1, l2):
    node = l1
    node_dict = {}

    while node:
        node_dict[node] = True
        node = node.next
    node = l2
    while node:
        if node in node_dict:
            return node
        node = node.next
    return None

def intersection_alt(l1, l2):
    if l1 is None or l2 is None:
        return None
    
    head1 = l1
    head2 = l2

    while l1 is not l2:
        if l1 is None:
            l1 = head2
        else:
            l1 = l1.next
        
        if l2 is None:
            l2 = head1
        else:
            l2 = l2.next
    
    return l1


class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

def main():
    print("Question 2.7\n")
    node = Node(70,None)
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    print(intersection_alt(head3, head4))
    

if __name__== "__main__":
    main()