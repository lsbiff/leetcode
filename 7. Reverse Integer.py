class Solution:
    def reverse(self, x: int) -> int:

        textNum = str(x)
        isNegative = False

        if textNum[0] == '-':
            isNegative = True

        textNum = textNum[::-1]

        if isNegative:
            textNum = textNum.replace('-', '')
            x = int(textNum) * -1
        else: 
            x = int(textNum)

        if x > 2147483647:
            return 0

        if x < -2147483648:
            return 0
        
        return x


tests = [123, 456, -123, -456, 0, 1, 9, 10, -10, 1000, -1000, 1098, 3901, 90123, -90123]

for test in tests:
    print(Solution.reverse(None, test))

#print(sys.maxsize)