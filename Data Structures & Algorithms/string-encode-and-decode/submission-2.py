class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded=[]
        for s in strs:
            if s:
                for c in s:
                    encoded.append(str(ord(c)))
            encoded.append("b")
        
        return ','.join(encoded)
        

    def decode(self, s: str) -> List[str]:
        if s:
            decoded=""
            ded=[]
            for strs in s.split(","):

                if strs == "b":
                    ded.append(decoded)
                    decoded=""
                else:
                    decoded += chr(int(strs))
            
            return ded
        return []
