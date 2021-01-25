'''
Approach 1
Use a list
'''
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = []

    def add(self, key: int) -> None:
        self.li.append(key)

    def remove(self, key: int) -> None:
        while key in self.li:
            self.li.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.li:
            return True
        else:
            return False

'''
Approach 2
'''
<Work In Progress>