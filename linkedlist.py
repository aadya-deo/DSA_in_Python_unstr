class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x):
        n = Node(x)

        if self.head == None:
            self.head = n
            return

        p = self.head

        while p.next != None:
            p = p.next

        p.next = n

    def delete(self):
        if self.head == None:
            print("Linked List is empty")
            return

        y = self.head.data
        self.head = self.head.next

        return y

    def display(self):
        if self.head == None:
            print("Linked List is empty")
            return

        p = self.head

        while p != None:
            print(p.data)
            p = p.next


l = LinkedList()

while True:
    ch = int(input("\n1 for insert \n2 for delete \n3 for display\nEnter the choice: "))

    if ch == 1:
        dat = input("Enter data to insert: ")
        l.insert(dat)

    elif ch == 2:
        print(f"The deleted node is {l.delete()}")

    elif ch == 3:
        l.display()

    else:
        break