class Solution(object):
    def romanToInt(self, s):
        r = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and r[s[i]] < r[s[i+1]]:
                ans -= r[s[i]]
            else:
                ans += r[s[i]]
        return ans



            
        