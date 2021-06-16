# def minion_game(string):
#     # your code goes here
#     string = string.lower()
#     kevin_count = 0
#     stuart_count = 0
#     if string.startswith('a') or string.startswith('e') or string.startswith('i') or string.startswith('o') or string.startswith('u'):
#         kevin_count += 1
#     else:
#         stuart_count += 1
#
#     for i in range(1, len(s)):
#         for j in range(len(s)-i+1):
#             x = string[j:i+j]
#             if x.startswith('a') or x.startswith('e') or x.startswith('i') or x.startswith('o') or x.startswith('u'):
#                 kevin_count += 1
#             else:
#                 stuart_count += 1
#             j += 1
#         i += 1
#
#     if kevin_count > stuart_count:
#         print('Kevin', kevin_count)
#     elif stuart_count > kevin_count:
#         print('Stuart', stuart_count)
#     else:
#         print('Draw')
#     # print(kevin_count, stuart_count)
#     # print(words)
#     # print(len(words))


def minion_game(string):
    # your code goes here
    s = string.lower()
    kevin_count = 0
    stuart_count = 0

    for i in range(len(s)):
        if s[i].startswith('a') or s[i].startswith('e') or s[i].startswith('i') or s[i].startswith('o') or s[i].startswith('u'):
            kevin_count += len(s) - i
        else:
            stuart_count += len(s) - i

    if kevin_count > stuart_count:
        print('Kevin', kevin_count)
    elif stuart_count > kevin_count:
        print('Stuart', stuart_count)
    else:
        print('Draw')
    # print(kevin_count, stuart_count)
    # print(words)
    # print(len(words))


if __name__ == '__main__':
    s = input()
    minion_game(s)
