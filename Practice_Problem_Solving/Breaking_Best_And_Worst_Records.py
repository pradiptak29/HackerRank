# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'breakingRecords' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts INTEGER_ARRAY scores as parameter.
# #
#
# def breakingRecords(scores):
#     # Write your code here
#     highest_score = [scores[0]]
#     lowest_score = [scores[0]]
#     for i in range(1, len(scores)):
#         for j in range(i):
#             if scores[i] > max(highest_score) and scores[i] not in lowest_score:
#                 highest_score.append(scores[i])
#             elif scores[i] < min(lowest_score) and scores[i] not in highest_score:
#                 lowest_score.append(scores[i])
#             else:
#                 pass
#
#     # print(highest_score)
#     # print(lowest_score)
#
#     highest_count = str(len(highest_score)-1)
#     lowest_count = str(len(lowest_score)-1)
#
#     return highest_count + " " + lowest_count
#
#
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input().strip())
#     scores = list(map(int, input().rstrip().split()))
#     result = breakingRecords(scores)
#     print(result)
#     # fptr.write(' '.join(map(str, result)))
#     # fptr.write('\n')
#     # fptr.close()


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest_score = [scores[0]]
    lowest_score = [scores[0]]
    for i in range(1, len(scores)):
        for j in range(i):
            if scores[i] > max(highest_score) and scores[i] not in lowest_score:
                highest_score.append(scores[i])
            elif scores[i] < min(lowest_score) and scores[i] not in highest_score:
                lowest_score.append(scores[i])
            else:
                pass

    # print(highest_score)
    # print(lowest_score)

    highest_count = str(len(highest_score) - 1)
    lowest_count = str(len(lowest_score) - 1)

    return highest_count, lowest_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
