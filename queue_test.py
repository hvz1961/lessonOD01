class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


# Пример использования очереди
if __name__ == "__main__":
    queue = Queue()

    print("Очередь пуста?", queue.is_empty())  # True

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Очередь после добавления элементов:", queue)  # [10, 20, 30]

    print("Первый элемент очереди:", queue.peek())  # 10

    print("Удаленный элемент:", queue.dequeue())  # 10
    print("Очередь после удаления элемента:", queue)  # [20, 30]

    print("Размер очереди:", queue.size())  # 2

    print("Очередь пуста?", queue.is_empty())  # False