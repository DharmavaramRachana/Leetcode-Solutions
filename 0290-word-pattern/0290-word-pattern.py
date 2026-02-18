class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for ch, w in zip(pattern, words):
            if ((ch in p2w and p2w[ch] != w) or (w in w2p and w2p[w] != ch)):
                return False

            p2w[ch] = w
            w2p[w] = ch

        return True