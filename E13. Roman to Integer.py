class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        i = 0

        while i < len(s):

            if s[i] == 'M':
                n = n + 1000   

            if s[i] == 'D':
                n = n + 500

            if s[i] == 'C':

                if i < len(s) - 1:
                    if s[i+1] == 'M':
                        i = i + 2
                        n = n + 900
                        continue
                        
                    if s[i+1] == 'D':
                        n = n + 400
                        i = i + 2
                        continue

                        
                n = n + 100
                

            if s[i] == 'L':
                n = n + 50
                

            if s[i] == 'X':

                if i < len(s) - 1:
                    if s[i+1] == 'C':
                        n = n + 90
                        i = i + 2
                        continue
                        
                    if s[i+1] == 'L':
                        n = n + 40
                        i = i + 2
                        continue
                        
                n = n + 10
                

            if s[i] == 'V':
                n = n + 5
                

            if s[i] == 'I':

                if i < len(s) - 1:

                    if s[i+1] == 'X':
                        n = n + 9
                        i = i + 2
                        continue

                    if s[i+1] == 'V':
                        n = n + 4
                        i = i + 2
                        continue
                        
                n = n + 1

            i = i + 1

        print(n)
        return n

Solution.romanToInt(None, "MCMXCIV")