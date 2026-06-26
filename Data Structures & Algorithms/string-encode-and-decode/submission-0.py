class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + ',' + word
        return s

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i != len(s):
            j = s.find(',', i)
            length = int(s[i:j])
            string_content = s[j+1: j+1+length]
            decoded_string.append(str(string_content))
            i = j + 1 + length
        return decoded_string
