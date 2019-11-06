def kth_to_last(head, pos):
    lead = head
    follow = head

    for _ in range(pos):
        if lead is None:
            return None
        lead = lead.next

    while lead is not None:
        lead = lead.next
        follow = follow.next
    return follow

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next


def main():
    print("Question 2.2\n")
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7, None)))))))
    print(kth_to_last(head, 3).data)

if __name__== "__main__":
    main()