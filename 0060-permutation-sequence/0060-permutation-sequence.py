class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1,n):
            numbers.append(i)
            fact *= i
        numbers.append(n)

        k = k - 1
        s = ''
        while True :
            s = s + str(numbers[k//fact])
            numbers.pop(k//fact)
            if len(numbers) <= 0:
                break
            k = k % fact
            fact = fact // len(numbers)
        return s