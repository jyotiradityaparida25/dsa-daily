import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts val into the multiset. 
        Returns True if the item was not present, False otherwise.
        """
        # Store index of newly added element
        self.idx_map[val].add(len(self.nums))
        self.nums.append(val)
        
        # Returns True if it was a new element (set size was 1 before insertion)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the multiset if present.
        Returns True if present, False otherwise.
        """
        if not self.idx_map[val]:
            return False
        
        # Index of element to remove
        remove_idx = self.idx_map[val].pop()
        last_val = self.nums[-1]
        
        # If the element to remove is not the last element, swap it
        if remove_idx != len(self.nums) - 1:
            self.nums[remove_idx] = last_val
            # Update index of last_val in idx_map
            self.idx_map[last_val].remove(len(self.nums) - 1)
            self.idx_map[last_val].add(remove_idx)
        
        # Pop the last element
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the collection.
        Probability is linearly related to count of values.
        """
        return random.choice(self.nums)