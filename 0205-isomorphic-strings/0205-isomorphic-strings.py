class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_s, iso_t = {}, {}

        for i in range(len(s)):
            ch_s, ch_t = s[i], t[i]
            if ch_s in iso_s and iso_s[ch_s] != ch_t:
                return False

            if ch_t in iso_t and iso_t[ch_t] != ch_s:
                return False

            if ch_s not in iso_s:
                iso_s[ch_s] = ch_t

            if ch_t not in iso_t:
                iso_t[ch_t] = ch_s

        return True