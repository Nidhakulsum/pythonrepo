def is_matching(exp):
    stack=[]
    for char in exp:
        if char in ["(","{","["]:
            stack.append(char)
        else :
            if not stack:
                return False
            current_char=stack.pop()
            if current_char=='(':
                if char!=')':
                    return False
            if current_char=='{':
                if char!='}':
                    return False
            if current_char=='[':
                if char!=']':
                    return False
    if stack:
        return False
    else:
        return True
exp="[}"
print(is_matching(exp))
exp="{}"
print(is_matching(exp))
