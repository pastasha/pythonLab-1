sides =[3,2,4,7,5,12,11,13,15,16,14,14]
sides=sorted(sides,reverse=True)
smax=0
for i in range(len(sides)):
    for j in range(len(sides)):
        for k in range(len(sides)):
            a=sides[i]
            b=sides[j]
            c=sides[k]
            if a+b>c and a+c>b and b+a>c:
                p=(a+b+c)/2
                s=round(((p*(p-a)*(p-b)*(p-c))**(1/2)).real,2)
                
                if s>smax:
                    smax=s
print(smax)
