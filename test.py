import sikfa


k = []
j=[]
for i in range(0,10):
    k.append(i)
    j.append(i**2)

ll = sikfa.find(k,j, 3, 50000, 1e-5)

for h in range(0, len(ll)):
    print(f'{ll[h].item()}x^{h}')
