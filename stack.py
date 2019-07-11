class Stack:
    def __init__(self):
        self._stack = []

    def lenstack(self):
        print(len(self._stack))
        print(self._stack)

    def push(self):
        p = input("Push")
        self._stack.append(p)
        print(self._stack)

    def pop(self):
        if len(self._stack) == 0:
            print("Stack is empty")
        else:
            self._stack.pop(-1)
            print(self._stack)

    def isempty(self):
        if len(self._stack) == 0:
            print("Empty")
        else:
            print("NO")
            print(self._stack)


    def inputfunc(self):

        print("Enter 1 - push")
        print("Enter 2 - pop")
        print("Enter 3 - length")
        print("Enter 4 - isEmpty?")
        print("Enter 5 - Show Stack")
        print("Enter 6 - Quit")


        while True:


              x = input("Enter Number")

              if x =="1":
                 self.push()

              elif x == "2":
                 self.pop()

              elif x=="3":
                 self.lenstack()

              elif x=="4":
                 self.isempty()

              elif x=="5":
                 self._stack

              elif x=="6":
                  break


stack1 = Stack()
stack1.inputfunc()