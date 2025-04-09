# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.maps = {}       

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.maps[tokenId] = currentTime + self.timeToLive        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.maps and self.maps[tokenId] > currentTime:
            self.maps[tokenId] = currentTime + self.timeToLive        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, time in self.maps.items():
            if time > currentTime:
                count += 1

        return count       


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)