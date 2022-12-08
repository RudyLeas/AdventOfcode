with open(r"C:\Users\lisku\Desktop\AdventOfCode\Day2\day2.txt","r" ) as f:
    rounds = f.readlines()
me=[]
opp=[]
sum=0
for i in range(0, len(rounds)):
    me.append(rounds[i][2])
    opp.append(rounds[i][0])
# own points for what I pick
for i in me:
    if(i=="X"):
        sum+=1
    if(i=="Y"):
        sum+=2
    if(i=="Z"):
        sum+=3
#points for the result of a round

for i in range(0, len(me)):
    if(ord(me[i])==ord(opp[i])+23):
        sum+=3
    if(me[i]=="X" and opp[i]=="C" or me[i]=="Y" and opp[i]=="A" or me[i]=="Z" and opp[i]=="B" ):
        sum+=6
print("Answer for Part I is: ",sum)
dict={
    "A":4,
    "B":5,
    "C":6
}
#part II 
newsum=0
for i in range(0, len(me)):
    if(me[i]=="Z"):
        if(opp[i]=="A"):
            newsum+=8
        if(opp[i]=="B"):
            newsum+=9
        if(opp[i]=="C"):
            newsum+=7
    if(me[i]=="Y"):
        newsum+=dict[opp[i]]
    if(me[i]=="X"):
        if(opp[i]=="A"):
            newsum+=3
        if(opp[i]=="B"):
            newsum+=1
        if(opp[i]=="C"):
            newsum+=2
print("answer for part II is: ",newsum)

