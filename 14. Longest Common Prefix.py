class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len(strs[0]) == 0:
            return ''

        currentChar = ''
        longestPrefix = ''
        index = 0

        minString = len(min(strs, key=len))

        while index < minString:

            currentChar = strs[0][index]

            for row in range(len(strs)):

                if currentChar != strs[row][index]:
                    return longestPrefix

            index += 1
            longestPrefix += currentChar

        return longestPrefix


tests = [["flower","flow","floght"], ["dog","racecar","car"], ["dog","dog"], ["dodg","doasdg","dogsasd"], ["","",""], ["asdafasf", "asdgsfdgs", "asdfasda", "asdsacasx", "asdrtwerfasd"]]

for test in tests:
    print(Solution.longestCommonPrefix(None, test))