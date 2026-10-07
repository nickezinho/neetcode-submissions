class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = []
        encoded_msg = ""
        for word in strs:
            length = str(len(word))
            msg.append(length)
            msg.append("#")
            msg.append(word)
        
        encoded_msg = "".join(msg)
        return encoded_msg 


    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        

        while idx < len(s):
            
            length = ""

            while s[idx].isdigit():
                length += s[idx]
                idx += 1
            idx += 1

            length = int(length)

            res.append(s[ idx: idx + length])
            
            idx += length

        return res

    

        

                


