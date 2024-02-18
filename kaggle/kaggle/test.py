# def solution(arr1, arr2):
#     u1 = 0
#     u2 = 0
#     if arr1[-1] != arr2[-1]:
#         return 'NO'
#
#     while len(arr1) > u1 and len(arr2) > u2:
#         if arr1[u1] == arr2[u2]:
#             u1 += 1
#             u2 += 1
#         elif arr1[u1 - 1] == arr2[u2]:
#             u2 += 1
#         elif arr1[u1] == arr2[u2 - 1]:
#             u1 += 1
#         else:
#             return 'NO'
#     return 'YES'
#
#
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
#
# print(solution(arr1, arr2))
#
#
# for i in range(1, 100):
#     for j in range(1, 100):
#         if i == j:
#             if solution(list(range(i)), list(range(j))) == 'NO':
#                 print('wrong', i, j)
#         else:
#             if solution(list(range(i)), list(range(j))) == 'YES':
#                 print('wrong', i, j)


f = open('../test/kinopoisk_input.txt')
f.readline()
a = list(map(int, f.readline().split()))
b = list(map(int, f.readline().split()))


def cosine_similarity1(vector1, vector2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    magnitude1 = (sum(v**2 for v in vector1))**0.5
    magnitude2 = (sum(v**2 for v in vector2))**0.5
    return dot_product / (magnitude1 * magnitude2)


print(cosine_similarity1(a, b))

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

a = np.array(a)
b = np.array(b)

cosine = cosine_similarity(a.reshape(1, -1), b.reshape(1, -1))

print(cosine)