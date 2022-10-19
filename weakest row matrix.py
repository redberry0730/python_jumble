
def kWeakestRows(mat, k):
    count = []
    for i ,j in enumerate(mat):
        result = (sum(j), i)
        count.append(result)
    count = sorted(count)
    # new = []
    # for i in range(k+1):
    #     new.append(count[i][1])
    # return new

    return (i[1] for i in count[:k])

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

print(kWeakestRows(mat, 3))