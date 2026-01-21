from math import dist

clasters_A=[[],[]]
A=[list(map(float, i.replace("\n", "").split())) for i in open("02_27_A.txt")]

clasters_B=[[],[], []]
B=[list(map(float, i.replace("\n", "").split())) for i in open("02_27_B.txt")]

for i in A:
    if (i[1]<90):
        clasters_A[0].append(i)
    else:
        clasters_A[1].append(i)

for i in B:
    if i[0]>10:
        if (i[1] < 31):
            clasters_B[0].append(i)
        elif (i[1]>41):
            clasters_B[2].append(i)
        else:
            clasters_B[1].append(i)

anti_A=[]
def anti(n):
    maxi=-1
    maxi_k=0
    for i in n:
        anti_t=sum(dist(i, p) for p in n)
        if (maxi<anti_t):
            maxi=anti_t
            maxi_k=i
    return maxi_k
print(sum(anti(clasters_A[1])), sum(anti(clasters_A[0])))

print(anti(clasters_B[2])[0], anti(clasters_B[0])[1])
