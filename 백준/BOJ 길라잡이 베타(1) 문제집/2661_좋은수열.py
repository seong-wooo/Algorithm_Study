# 백트래킹이 뭔지 공부부터하기

# n = int(input())
#
# def dfs(string, s):
#     string += s
#     # i가 들어와도 되는지 검사하기
#     if len(string) != 0:
#         for i in range(len(string)//2):
#             if string[-2-2*i:-1-i] == string[-1-i:]:
#                 return None
#
#     if len(string) == n:
#         return string
#
#
#     if s == "1":
#         a = dfs(string,"2")
#         if a is None:
#             a = dfs(string,"3")
#             if a is None:
#                 a = dfs(string[:-1], "2")
#                 if a is None:
#                     a = dfs(string[:-1], "3")
#
#
#     elif s == "2":
#         a = dfs(string,"1")
#         if string is None:
#             a = dfs(string,"3")
#             if a is None:
#                 a = dfs(string[:-1], "1")
#                 if a is None:
#                     a = dfs(string[:-1], "3")
#
#     else:
#         a = dfs(string,"1")
#         if string is None:
#             a = dfs(string,"2")
#             if a is None:
#                 a = dfs(string[:-1], "1")
#                 if a is None:
#                     a = dfs(string[:-1], "2")
#
#     if a is None:
#         return None
#
#     return a
#
# string = ""
# print(dfs(string,"1"))
#
