class Queue:
    def __init__(self):
        self.F = -1
        self.R = -1
        self.qt = [0] * 5

    def insert(self, x):
        if self.R == 4:
            print("Queue is overflow")
            return

        self.R = self.R + 1
        self.qt[self.R] = x

        if self.F == -1:
            self.F = 0

    def delete(self):
        if self.F == -1:
            print("Queue is underflow, nothing to delete.")
            return

        y = self.qt[self.F]

        if self.F == self.R:
            self.F = self.R = -1
        else:
            self.F = self.F + 1

        return y

    def display(self):
        if self.F == -1:
            print("Queue is empty")
            return

        for i in range(self.F, self.R + 1):
            print(self.qt[i])


q = Queue()

while True:
    ch = int(input("\n1 for insert \n2 for delete \n3. for display\nEnter the choice: "))

    if ch == 1:
        dat = input("Enter data to insert in queue: ")
        q.insert(dat)

    elif ch == 2:
        print(f"The deleted node is {q.delete()}")

    elif ch == 3:
        q.display()

    else:
        break