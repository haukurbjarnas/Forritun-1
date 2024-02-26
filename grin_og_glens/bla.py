class Node:

    def __init__(self, data = None, next = None):

        self.data = data

        self.next = next

 

def print_list(head):

    if head != None:

        print(head.data, end= " ")

        print_list(head.next)

    else:

        print("")

 

#Example program:

head = Node("A", Node("B", Node("C", Node("D", None))))

print_list(head)

# output: A B C D



tail = Node("D", None)

head = Node("A", Node("B", Node("C", tail)))




node = head

head = tail

tail = node

head.next = tail.next

tail.next = None



print_list(head)