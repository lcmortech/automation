class DynamicArray:
   
   def __init__(self):
       self.capacity = 1
       self.size = 0
       self.array = [None] * self.capacity

   def _resize(self, new_capacity):
       new_array = [None] * new_capacity
       for i in range(self.size):
           new_array[i] = self.array[i]
       self.array = new_array
       self.capacity = new_capacity

   def append(self, value):
       if self.size == self.capacity:
           self._resize(self.capacity * 2)
       self.array[self.size] = value
       self.size += 1

   def pop(self):
       if self.size == 0:
           raise IndexError("Pop from empty array")
       self.size -= 1
       self.array[self.size] = None
       if self.size > 0 and self.size == self.capacity // 4:
           self._resize(self.capacity // 2)

   def insert(self, index, value):
       if self.size == self.capacity:
           self._resize(self.capacity * 2)
       for i in range(self.size, index, -1):
           self.array[i] = self.array[i - 1]
       self.array[index] = value
       self.size += 1

   def delete(self, index):
       for i in range(index, self.size - 1):
           self.array[i] = self.array[i + 1]
       self.array[self.size - 1] = None
       self.size -= 1
       if self.size > 0 and self.size == self.capacity // 4:
           self._resize(self.capacity // 2)

# METHODS:
# resize
# append
# pop
# insert
# delete

# Key Operations & Complexity
# Append: O(1) amortized, O(n) on resize.
# Insert/Delete at index: O(n) due to shifting elements.
# Search: O(n) for unsorted arrays.
# Resize: Expensive (O(n)) but infrequent due to doubling strategy [2],[3].

# Advantages:
# Flexible size management.
# Efficient amortized append performance.
# Considerations:
# Resizing involves costly copy operations.
# Choosing the right growth factor balances memory usage and performance [2].