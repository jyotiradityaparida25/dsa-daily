# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        
        self._has_next = self.iterator.hasNext()
        self._next_val = self.iterator.next() if self._has_next else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next_val

    def next(self):
        """
        :rtype: int
        """
        value_to_return = self._next_val
        
        # Advance the underlying iterator to refill our cache
        self._has_next = self.iterator.hasNext()
        self._next_val = self.iterator.next() if self._has_next else None
            
        return value_to_return

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].