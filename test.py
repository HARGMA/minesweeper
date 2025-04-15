from numpy import array

# Define the initial array
m = array([['💣', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '💣', '0', '0', '0', '0', '0', '0', '💣'],
           ['0', '0', '💣', '0', '0', '0', '💣', '0', '0', '0'],
           ['0', '💣', '0', '0', '0', '0', '0', '💣', '0', '0'],
           ['💣', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '💣', '0', '0', '0', '0', '0', '0', '💣'],
           ['0', '0', '💣', '0', '0', '0', '💣', '0', '0', '0'],
           ['0', '💣', '0', '0', '0', '0', '0', '💣', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0', '0', '💣', '0'],
           ['0', '0', '0', '0', '0', '0', '0', '0', '💣', '0']]
          )
m1 = array([['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '1', '0', '0', '0', '0', '0', '0', '1'],
            ['0', '0', '1', '0', '0', '0', '1', '0', '0', '0'],
            ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0'],
            ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '1', '0', '0', '0', '0', '0', '0', '1'],
            ['0', '0', '1', '0', '0', '0', '1', '0', '0', '0'],
            ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0']]
           )


def coins(i, j):
    s = "💣"
    if m[i, j] != "💣":
        x = abs(i - 1)
        y = abs(j - 1)
        s = int(m1[x, y]) + int(m1[x, j]) + int(m1[i, y])
    return s


#
# m[0,0]=str(coins(0,0))
# m[0,9]=str(coins(0,9))
# m[9,0]=str(coins(9,0))
# m[9,9]=str(coins(9,9))
# for i in range(1,9):
#         for j in range(1,9):
#             if m[i,j]!="💣":
#                 m[i,j]=calcul(m,i,j)


# def right_edge(m,l):
#     for x in range(1,9):
#         s=0
#         if m[x,l]!="💣":
#             for i in range(x-1,x+2):
#                 for j in range(0,2):
#                     if (i!=x or j!= l) and m[i,j]=="💣":
#                         s=s+1
#             m[x,l]=str(s)
#
# def left_edge(m,l):
#     for x in range(1,9):
#         s=0
#         if m[x,l]!="💣":
#             for i in range(x-1,x+2):
#                 for j in range(8,10):
#                     if (i!=x or j!= l) and m[i,j]=="💣":
#                         s=s+1
#             m[x,l]=str(s)
# def column(m,l,beg,end):
#     for x in range(1,9):
#         s=0
#         if m[x,l]!="💣":
#             for i in range(x-1,x+2):
#                 for j in range(beg,end):
#                     if (i!=x or j!= l) and m[i,j]=="💣":
#                         s=s+1
#             m[x,l]=str(s)
#
# def row(m,c,beg,end):
#     for y in range(1,9):
#         s=0
#         if m[c,y]!="💣":
#             for i in range(beg,end):
#                 for j in range(y-1,y+2):
#                     if (i!=c or j!=y) and m[i,j]=="💣":
#                         s=s+1
#             m[c,y]=str(s)
#
# # def up_edge(m,c):
# #     for y in range(1,9):
# #         s=0
# #         if m[c,y]!="💣":
# #             for i in range(0,2):
# #                 for j in range(y-1,y+2):
# #                     if (i!=c or j!=y) and m[i,j]=="💣":
# #                         s=s+1
# #             m[c,y]=str(s)
# #
# # def lower_edge(m,c):
# #     for y in range(1,9):
# #         s=0
# #         if m[c,y]!="💣":
# #             for i in range(8,10):
# #                 for j in range(y-1,y+2):
# #                     if (i!=c or j!=y) and m[i,j]=="💣":
# #                         s=s+1
# #             m[c,y]=str(s)
#
# column(m,0,0,2)
# column(m,9,8,10)
# row(m,0,0,2)
# row(m,9,8,10)

def calcul(m, i, j):
    s = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < 10 and 0 <= y < 10 and (x != i or y != j) and m[x, y] == "💣":
                s = s + 1
    return str(s)


for i in range(10):
    for j in range(10):
        if m[i, j] != "💣":
            m[i, j] = calcul(m, i, j)


print(m)
# print(m1)
