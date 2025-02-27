class LimitedQueue:

    def __init__(self, max_n):
        self.max_n = max_n
        self.queue = [None] * self.max_n
        self.head = 0  # Голова указывает на индекс 0
        self.tail = 0  # Хвост указывает на индекс 0
        self.size = 0  # При создании очередь пуста, её длина - 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, value):
        if self.queue[self.tail] is not None:
            self.head = (self.head + 1) % self.max_n
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size < self.max_n:
            self.size += 1
  

        
numbers = LimitedQueue(3)
numbers.push(12)
numbers.push(24)
numbers.push(34)
numbers.push(44)
numbers.push(54)
numbers.push(62)
numbers.push(72)
print(numbers.head)
print(numbers.tail)
print(numbers.size)
print(numbers.queue)