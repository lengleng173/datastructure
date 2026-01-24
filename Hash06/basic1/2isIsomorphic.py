class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        dic1=dict()
        dic2=dict()
        for idx,i in enumerate(s):
            if i in dic1.keys():
                if t[idx]!=dic1[i]:return False
            if t[idx] in dic2.keys():
                if i!=dic2[t[idx]]:return False
            else:
                dic1[i]=t[idx]
                dic2[t[idx]]=i
        return True