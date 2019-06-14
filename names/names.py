import time

start_time = time.time()

class BinarySearchTree:
  def __init__(self, value = ''):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      if value < self.value:
          if not self.left:
              self.left = BinarySearchTree(value)
          else:
              self.left.insert(value)
      elif value >= self.value:
          if self.right is None:
              self.right = BinarySearchTree(value)
          else:
              self.right.insert(value)

  def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

tree = BinarySearchTree()

for i in names_1:
  tree.insert(i)

for j in names_2:
  if tree.contains(j):
    duplicates.append(j)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

