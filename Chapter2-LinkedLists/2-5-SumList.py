#if lists are same length
def sum_list(l1, l2):
    digits = 0
    sum = 0
    while l1 and l2:
        print("l1: " + str(l1.data) + " l2: " + str(l2.data) + " digits: " + str(digits))
        sum += (l1.data + l2.data) * (10 ** digits)
        digits += 1
        l1 = l1.next
        l2 = l2.next

    return sum

#if list are different length
def sum_list_diff(l1, l2):
    l1_head = l1
    l2_head = l2

    res_node = None
    res_head = None


    carry = 0
    while l1 or l2 or carry:
        result = carry
        if l1:
            result += l1.data
            l1 = l1.next
        if l2:
            result += l2.data
            l2 = l2.next
        if res_node:
            res_node.next = Node(result % 10)
            res_node = res_node.next
        else:
            res_node = Node(result % 10)
            res_head = res_node
        carry = result / 10
    
    return res_head
    

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

def main():
    print("Question 2.5\n")
    list1 =  Node(1,Node(2,Node(3)))
    list2 = Node(4,Node(9,Node(5)))

    #print(sum_list(list1, list2))
    new_list = sum_list_diff(list1, list2)
    while new_list:
        print(new_list.data)
        new_list = new_list.next

    

if __name__== "__main__":
    main()