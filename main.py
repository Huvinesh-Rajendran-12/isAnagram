class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}     
        hashmapT = {}
        if len(s) != len(t):
            return False
        for i,s_ in enumerate(s):
            if s_ not in hashmapS:
                hashmapS[s_] = s.count(s_)
        for i,t_ in enumerate(t):
            if t_ not in hashmapT:
                hashmapT[t_] = t.count(t_)
        # breakpoint()
        for x in hashmapS:
            if x not in hashmapT:
                return False
            elif hashmapS[x] != hashmapT[x]:
                return False
            else:
                continue
        return True
        

solution = Solution()
print(solution.isAnagram("aacc","ccac"))