#H65 - Valid Number

class Solution:
    def isNumber(self, s: str) -> bool:

        bNumberFound = False
        currentIndex = 0
        bDotFound = False
        bExponentFound = False
        strLen = len(s)
    
        # first character must be [number . + -]
        if not s[0].isnumeric():
            if strLen == 1:
                return False
            currentIndex = 1
            if s[0] == '.':
                bDotFound = True
            elif s[0] != '+' and s[0] != '-':
                return False     
        
        
        # keep looking for numbers [0-9]
        for i in range(currentIndex, strLen):

            if not s[i].isnumeric():
                break
            currentIndex = currentIndex + 1
            bNumberFound = True

        if currentIndex >= strLen:
            return True

        if s[currentIndex] != '.' and s[currentIndex] != 'e' and s[currentIndex] != 'E':
            return False

        # found a [. e E]
        # if found . but already found one
        if s[currentIndex] == '.':
            if bDotFound:
                return False
            else:
                bDotFound = True
                currentIndex = currentIndex + 1

                if currentIndex >= strLen:
                    if bNumberFound:
                        return True
                    else:
                        return False
            

        # if found [e E]
        if s[currentIndex] == 'e' or s[currentIndex] == 'E':

            # you can only stack [e E] if you already found a number
            if not bNumberFound:
                return False

            bExponentFound = True

            currentIndex = currentIndex + 1

            if currentIndex >= strLen:
               return False

            # after [e E] you could gave [+ -]
            if s[currentIndex] == '+' or s[currentIndex] == '-':
                currentIndex = currentIndex + 1

                if currentIndex >= strLen:
                    return False    

        # keep looking for numbers. this part could be after the first [.] found and could have not found and [e E] yet
        for i in range(currentIndex, strLen):

            if not s[i].isnumeric():
                break
            currentIndex = currentIndex + 1
            bNumberFound = True

        if currentIndex >= strLen:
            return True

        # found [.] but at this point you already have found one
        if s[currentIndex] == '.':
            return False
        
        # by this point you can only have found [e E] 
        if s[currentIndex] == 'e' or s[currentIndex] == 'E':

            # you can only stack [e E] if you already found a number
            if not bNumberFound:
                return False

            # if you already found [e E] before 
            if bExponentFound:
                return False

            else:
                bExponentFound = True
                currentIndex = currentIndex + 1

                if currentIndex >= strLen:
                    return False    

                # after [e E] you could gave [+ -]
                if s[currentIndex] == '+' or s[currentIndex] == '-':
                    currentIndex = currentIndex + 1

                    if currentIndex >= strLen:
                        return False
                    
        else:
            return False

        # keep looking for numbers. here you are just looking for numbers after [e E] and nothing more
        for i in range(currentIndex, strLen):

            if not s[i].isnumeric():
                break
            currentIndex = currentIndex + 1

        # if you get a break by a non number, return invalid
        if currentIndex >= strLen:
            return True
        else:
            return False

valid = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "-.3e6"]
notValid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", '0.e', '1.e+', '.e+', '0e', '..2', '+.', '.+', '..', '+e', '-e', '10ee', '-29.2ee+19', '10e', '.', '.e1']

print('============= VALID ============')

for v in valid:
    print(f'{Solution.isNumber(None, v)}: {v}')

print('============= NOT VALID ============')
for nv in notValid:
    print(f'{Solution.isNumber(None, nv)}: {nv}')