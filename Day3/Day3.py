with open(r"C:\Users\lisku\Desktop\AdventOfCode\Day3\day3.txt","r" ) as f:
    compartments = f.readlines()
comp1= []
comp2= []
for count,i in enumerate (compartments):
    comp1.append(i[:len(i)//2])
    comp2.append(i[len(i)//2:])


def priority(a):
    val=ord(a)
    if(val>96):
        return(val-96)
    if(val<91):
        return(val-38)
letters=[]
for i in range(0,len(comp1)):
    for j in comp1[i]:
        if j in comp2[i]:
            letters.append(j)
            break
sum=0
for i in range(len(letters)):
    sum+=priority(letters[i])
print(sum)



