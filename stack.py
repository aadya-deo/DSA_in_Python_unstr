class Stack:
    def __init__(self):
        self.top = -1
        self.st = [0] * 5

    def push(self, x):
        if self.top == 4:
            print("Stack is overflow")
            return

        self.top = self.top + 1
        self.st[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack is underflow, nothing to pop.")
            return

        y = self.st[self.top]
        self.top = self.top - 1

        return y

    def display(self):
        if self.top == -1:
            print("Stack is empty")
            return

        for i in range(self.top, -1, -1):
            print(self.st[i])


s = Stack()

while True:
    ch = int(input("\n1 for push \n2 for pop \n3 for display\nEnter the choice: "))

    if ch == 1:
        dat = input("Enter data to push in stack: ")
        s.push(dat)

    elif ch == 2:
        print(f"The popped element is {s.pop()}")

    elif ch == 3:
        s.display()

    else:
        break