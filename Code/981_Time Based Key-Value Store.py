'''
Approach

'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.arr.get(key, None)
        if A is None:
            return ""
        print(A)
        i = bisect.bisect(A, (timestamp, chr(127)))
        #print(chr(127))
        print(i)
        return A[i-1][1] if i else ""