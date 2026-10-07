class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []
        for ch in first:
            l, r = first[ch], last[ch]
            valid = True
            i = l
            while i <= r:
                if first[s[i]] < l:
                    valid = False
                    break
                r = max(r, last[s[i]])
                i += 1
            if valid:
                valid_intervals.append((r, l))

        valid_intervals.sort()

        ans = []
        prev_end = -1
        for r, l in valid_intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans