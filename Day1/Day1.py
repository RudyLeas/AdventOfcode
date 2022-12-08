with open(r"C:\Users\lisku\Desktop\AdventOfCode\Day1\day1.txt","r" ) as f:
    contents = f.readlines()
cal= []
cal.append(0)    
index=0
for i in range(len(contents)):

    
    if contents[i]=="\n":
        index=index+1
        cal.append(0)
    else:
        cal[index]+=int(contents[i].replace('\n',''))
print("Part I: "+str(max(cal)))
print("Part II: "+str(sum((sorted(cal)[-3:]))))



        


