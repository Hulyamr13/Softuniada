def longest_valid_parentheses(s):
    stack = []
    result = 0

    for i in range(len(s)):
        c = s[i]
        if c == ')':
            if stack and stack[-1][0] == 0:
                stack.pop()
                result = max(result, i - (-1 if not stack else stack[-1][1]))
            else:
                stack.append((1, i))
        else:
            stack.append((0, i))

    return result


text = input()
print(longest_valid_parentheses(text))
