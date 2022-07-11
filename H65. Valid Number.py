#H65 - Valid Number

class Solution:
    def isNumber(self, s: str) -> bool:
        startIndex = 0
        currentIndex = 0
        bExponentFound = False
        bDotFound = False
        strLength = len(s)

        if not s[0].isnumeric():

            if s[0] != '+' and s[0] != '-':
                if s[0] != '.':
                    return False
                else:
                    bDotFound = True
                    if strLength == 1:
                        return False
                    startIndex = currentIndex = 1


            else:
                if strLength == 1:
                    return False

                startIndex = currentIndex = 1

        for i in range(startIndex, strLength):
            #print(i)

            if not s[i].isnumeric():
                break

            currentIndex = currentIndex + 1

        if currentIndex >= strLength:
            return True


        if s[currentIndex] != '.':
            if s[currentIndex] != 'e' and s[currentIndex] != 'E':
                return False
            if bDotFound:
                if s[currentIndex - 1] == '.':
                    return False
            bExponentFound = True
        else:
            if bDotFound == True:
                return False

            if strLength == 2 and not s[0].isnumeric():
                return False

        currentIndex = currentIndex + 1

        if currentIndex >= strLength:
            if bExponentFound == True:
                return False

            return True

        if bExponentFound:
            if s[currentIndex] == '+' or s[currentIndex] == '-':
                currentIndex = currentIndex + 1

        if currentIndex >= strLength:
            return True

        for i in range(currentIndex, strLength):

            if not s[i].isnumeric():
                if bExponentFound:
                    if s[i] == '.':
                        return False
                break

            currentIndex = currentIndex + 1

        if currentIndex >= strLength:
            return True

        if not bExponentFound:
            if s[currentIndex] != 'e' and s[currentIndex] != 'E':
                return False

        currentIndex = currentIndex + 1

        for i in range(currentIndex, strLength):

            if not s[i].isnumeric():
                break

            currentIndex = currentIndex + 1

        return True