class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for str in strs:
            temp += str + "\n"
        return temp
    def decode(self, s: str) -> List[str]:
        new = []
        temp = ""
        for i in s:
            if(i == "\n"):
                new.append(temp)
                temp = ""
            else:
                temp += i
        return new