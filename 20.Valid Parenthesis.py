#20. Valid Parenthesis
# use stack

def isValid(s: str) -> bool:

    if len(s) % 2 == 1:
        return False

    stack = []

    for c in s:

        if c == '(':
            stack.append(c)
            continue

        if c == '[':
            stack.append(c)
            continue

        if c == '{':
            stack.append(c)
            continue

        if len(stack):

            if c == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
            
            if c == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False

            if c == ')':
                
                if stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
                
        else:
            if c == ')' or c == ']' or c == '}':
                return False


    if len(stack):
        return False

    return True

tests = ["()", "()[]{}", "(]", "{", "((", "()[]{}", "){", "))"]
for test in tests:
    print(isValid(test))
