'''
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        res = []
        if n > 1:
            for i in range(2, n):
                if self.isPrime(i)==True:
                    res.append(i)
        return len(res)
    
    def isPrime(self, n):
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

'''
Optimization in terms of no. of loops
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        res = []
        if n > 1:
            for i in range(2, n):
                if self.isPrime(i)==True:
                    res.append(i)
        return len(res)
    
    def isPrime(self, n):
        if n//2 >= 2:
            for i in range(2, n//2+1):
                if n%i == 0:
                    return False
        return True

'''
Sieve of Eratosthenes
Time: O(n log log n)
Space: O(n)
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        prime_arr = [True] * (n+1)
        for i in range(2, int(math.sqrt(n))+1):
            if prime_arr[i] == True:
                j = i*i
                while j <= n:
                    prime_arr[j] = False
                    j += i
        count = 0
        for i in prime_arr[2:-1]:
            if i == True:
                count += 1
        return count
