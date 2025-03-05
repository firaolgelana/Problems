# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        min_number = 0
        for keys in count:
            min_number += (keys + 1) * (math.ceil(count[keys] / (keys + 1))) 
        
        return min_number
        