class Solution:

    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            # Format: <length>#<string>
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the delimiter '#' separating length and content
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the upcoming string
            length = int(s[i:j])

            # Slice the string of known length
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # Move pointer to the next encoded block
            i = end

        return res