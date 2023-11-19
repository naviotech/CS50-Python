class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.cookie = "🍪"
        self.size = size
    def __str__(self):
        cookies = self.cookie * self.size
        return f"{cookies}"

    def deposit(self, n):
        if n <= (self.capacity - self.size):
         self.size += n
        else:
            raise ValueError
        
    def withdraw(self, n):
        if n <= self.size:
         self.size -= n
        else:
            raise ValueError
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Size cannot be negative")
        self._size = size


def main():
    cookies=Jar(12)
    cookies.deposit(12)
    cookies.withdraw(6)
    print(cookies.capacity)
    print(cookies)


if __name__ == "__main__":
    main()