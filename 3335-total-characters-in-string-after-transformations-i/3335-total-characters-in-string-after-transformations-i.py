class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        my_dict = Counter(s)

        for _ in range(t):
            temp = {}
            for val in my_dict:
                count = my_dict[val]
                if val != 'z':
                    key = chr(ord(val) + 1)
                    temp[key] = (temp.get(key, 0) + count) % MOD
                else:
                    temp['a'] = (temp.get('a', 0) + count) % MOD
                    temp['b'] = (temp.get('b', 0) + count) % MOD
            my_dict = temp

        return sum(my_dict.values()) % MOD

                    