class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.capacity > self.current:
      del self.storage[self.current]
      self.storage.insert(self.current, item)
      self.current += 1

    elif self.capacity == self.current:
      self.current = 0
      self.append(item)

  def get(self):
    array = []
    for x in self.storage:
      if x != None:
        array.append(x)
    return array

# Add your answers to the questions below.

# 1. What is the runtime complexity of your ring buffer's `append` method? 
# O(1) complexity

# 2. What is the space complexity of your ring buffer's `append` function? 
# O(1)

# 3. What is the runtime complexity of your ring buffer's `get` method? 
# O(n)

# 4. What is the space complexity of your ring buffer's `get` method? 
# O(n)

# 5. What is the runtime complexity of the provided code in `names.py`? 
# O(n^2)

# 6. What is the space complexity of the provided code in `names.py`? 
# O(n^2)

# 7. What is the runtime complexity of your optimized code in `names.py`? 
# O(n)

# 8. What is the space complexity of your optimized code in `names.py`? 
# O(n)
