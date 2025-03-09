# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = deque()
        for card in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)
        
        ans = [card for card in queue]
        return ans
        