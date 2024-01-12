from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            s_encoded = " ".join(map(lambda x: str(ord(x)), s))
            encoded = ";".join([encoded, s_encoded]) if encoded != "" else s_encoded

        return encoded

    def decode(self, str: str) -> List[str]:
        splitted = str.split(";")
        decoded = []
        for s in splitted:
            s_splitted = s.split(" ")
            s_decoded = "".join(map(lambda x: chr(int(x)), s_splitted))

            decoded.append(s_decoded)

        return decoded


encoded = Solution().encode(["lint", "co, de", '""', "lo;;;;;;ve", "you"])
print(encoded)
decoded = Solution().decode(encoded)
print(decoded)
