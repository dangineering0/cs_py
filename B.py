'''
g = [5,8,1,2,9], b = 22 => c = ?
22/5 = 4.4
    [5,x,1,2,x]

    [5,8,9], remaining = b - 3 == 19

    x = 19/3 = 6 1/3

    [8,9] reaminig = b - 1 =

22 - 3 = 19/3 = 6 1/3
22 - 8 = 14/2 = 7

4.4, 4.4 [2, 6]
g = [10,20,30] b= 30 c= 10
g= [.5,5,10.2,1000.55] b = 10 c =2.5
.5 < 2.5 => 2 / n-1 == > c= 3.166
c = 4.5 -> [.5, 3.1, 3.1, 3.1]

g = [1,10,100, 1000, 10001] b = 10 c = 2.25
1, 2, 2, 2,
g = [2,4,5,10,11] b = 4

c = .8

sU = 0
numC = 5
c = (4/5) + (0/3) = .8

sumUncapped = 1
numCapped = 4
c = b/len(g) + sumUn / numCp

c = b/len(g) + (sumUn / numCp)

'''


# @param list of ints, budget b
# @return int c
def find_budget(g, b):  [2, 4, 5, 10, 11]


b = 15
# 2,3.5,3.5, 3.5, 3.5
c = b / len(g)

sumUncapped = 0  # 2
numCapped = 0  # 1
c = 3
for x in g:
    if x <= c:
        sumUncapped += x
    else:
        numCapped += 1
    if numCapped != 0:
        c = c + (sumUncapped / numCapped)
        sumUncapped = 0
        numCapped = 0
        # c = 3
return c


# shortest solution

def awardCuts(arr, b):
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()  # O(nlogn) time
    prefSum = 0

    for i in range(n):
        c = arr[i]
        tot = prefSum + (n - i) * c
        if tot == b:
            return c
        elif tot > b:
            return (b - prefSum) * 1.0 / (n - i)
        prefSum += arr[i]

    return arr[n - 1]


dfobox @ gmail.com
Ivan
