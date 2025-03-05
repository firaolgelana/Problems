# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        for i in range(size):
            left, middle = flowerbed[i-1], flowerbed[i]
            right = flowerbed[i+1] if i < size - 1 else 0
            if i == 0 and middle == 0 and size == 1:
                n -= 1
            elif i == 0 and middle == right == 0:
                n -= 1
                flowerbed[i] = 1
            elif i == size -1 and left == middle == 0:
                n -= 1
            elif left == middle == right == 0:
                flowerbed[i] = 1
                n -= 1

        return n < 1