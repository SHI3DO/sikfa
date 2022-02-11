import sikfa

k = []
j=[]
for i in range(0,10):
    k.append(i)
    j.append(i**2)

sikfa.find(k,j, 3, 200000, 1e-6)