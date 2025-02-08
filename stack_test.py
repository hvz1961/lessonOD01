class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


# Пример использования стека
if __name__ == "__main__":
    stack = Stack()

    print("Стек пуст?", stack.is_empty())  # True

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Стек после добавления элементов:", stack)  # [10, 20, 30]

    print("Верхний элемент стека:", stack.peek())  # 30

    print("Удаленный элемент:", stack.pop())  # 30
    print("Стек после удаления элемента:", stack)  # [10, 20]

    print("Размер стека:", stack.size())  # 2

    print("Стек пуст?", stack.is_empty())  # False