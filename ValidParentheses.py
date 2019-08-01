def isValid(s):
    container = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for i in s:
        if i in container.keys():
            stack.append(i)
        else:
            if stack:
                pop = stack.pop()
                if container[pop] !=i:
                    print('false')
            else:
                print('false')
    if stack:
        print('false')
    else:
        print('true')

# def isValid_1(s):
#     if not s:
#         print('true')
#         return True
#
#     stack = []
#     container = {'(': ')', '[': ']', '{': '}'}
#     for paren in s:
#         if paren in container.keys():
#             stack.append(paren)
#         else:
#             if stack:
#                 left = stack.pop()
#                 if container[left] != paren:
#                     return False
#             else:
#                 return False
#     if stack:
#         return False
#     else:
#         return True
if __name__ == "__main__":
    s = '()'
    isValid_1(s)