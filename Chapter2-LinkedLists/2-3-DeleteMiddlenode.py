def remove_middle_node(head):
    slow = head
    fast = head
    count = 0

    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        count += 1
    
    tmp = head
    for i in range(count-1):
        tmp = tmp.next

    tmp.next = tmp.next.next 
    
    return head

def middle_node(head):
    tmp = head
    while tmp and tmp.next:
        head = head.next
        tmp = tmp.next.next
    return head

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next


def main():
    print("Question 2.2\n")
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7, None)))))))
    og = head

    # while og:
    #     print(og.data)
    #     og = og.next
    
    # remove_middle_node(head)

    # print("--------")
    # tmp = head

    # while tmp:
    #     print(tmp.data)
    #     tmp = tmp.next
    print(middle_node(head).data)
    

if __name__== "__main__":
    main()