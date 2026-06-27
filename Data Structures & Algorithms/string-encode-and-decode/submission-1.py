class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=''
        for st in strs:
            encoded+=st+",!@#";
        return encoded;    

    def decode(self, s: str) -> List[str]:
        decoded=s.split(",!@#")
        return decoded[:len(decoded)-1]