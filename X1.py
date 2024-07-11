def balance_brackets(s):
    stack = []
    remove = set()

    for i, char in enumerate(s):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if stack and ((char == ")" and stack[-1][0] == "(") or 
                          (char == "]" and stack[-1][0] == "[") or 
                          (char == "}" and stack[-1][0] == "{")):
                stack.pop()
            else:
                remove.add(i)
    
    while stack:
        remove.add(stack.pop()[1])

    result = ''.join([char for i, char in enumerate(s) if i not in remove])
    
    return result

input_data = input("qavslarni kiriting: ")

print(balance_brackets(input_data))

