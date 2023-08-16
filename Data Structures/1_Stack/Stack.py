class Stack:
  def __init__(self):
    self.items =[] # create an empty list in constructor

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if(self.is_empty == False):
      raise IndexError("pop from empty stack")
    else:
      return self.items.pop()

  def peek(self): # peeking top element
    if not self.is_empty():
      return self.items[-1]

  def is_empty(self):
    if len(self.items) == 0:
      return True
    else:
      return False

  def size(self):
    return len(self.items)



# driver code

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)


print("Top element is: " + str(stack.peek()))
print("Element popped is: " +  str(stack.pop()))
print("Stack empty? : "+  str(stack.is_empty()))
print("Stack size: " +  str(stack.size()))

#######################################

# using stack without implementation using a list



stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

top_el = stack[-1]
print("Top stack element is: "+str(top_el))

popped = stack.pop()
print("Popped item is: "+str(popped))

if not stack:
  print("Empty stack")
