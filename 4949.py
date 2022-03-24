
while True:
    s = input()
    if s == '.':
        break
    
    stack=[]
    for i in s:
        if i == '.' and stack:
            print('no')
            break
        if i == '(' or i =='[':
            stack.append(i)
        elif i ==')':
            if not stack:
                print('no')
                break
            if stack[-1]!='(':
                print('no')
                break
            stack.pop()
        elif i==']':
            if not stack:
                print('no')
                break
            if stack[-1]!='[':
                print('no')
                break
            stack.pop()
    else:
        print('yes')
    
