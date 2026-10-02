class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False


        fs={}
        for x in s:
            fs[x]= fs.get(x,0)+1

        
        for ts in t:

            if(ts in fs and fs[ts]!=0):
                fs[ts]= fs[ts]-1
            else:
                return False

        return True


        

        