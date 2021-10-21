print("---------------------1st--------------------------")

for i in range(1,6):
    for j in range(1,6):
        if(j>=1 and j<=i):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("---------------------2nd--------------------------")
for i in range(1,6):
    for j in range(1,6):
        if(j>=6-i and j<=5):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("---------------------3rd--------------------------")
for i in range(1,6):
    for j in range(1,6):
        if(j>=1 and j<=6-i):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("----------------------4th-------------------------")
for i in range(1,6):
    for j in range(1,6):
        if(j>=i and j<=5):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("-----------------------5th------------------------")
for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("----------------------6th-------------------------")
for i in range(1,6):
    for j in range(1,10):
        if(j>=i and j<=10-i):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("----------------------7th-------------------------")
for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end="")
        else:
            print(end=" ")
    print()
for i in range(1,6):
    for j in range(1,10):
        if(j>=i and j<=10-i):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("----------------------8th-------------------------")
for i in range(1,6):
    for j in range(1,11):
        if(j>=1 and j<=i or j>=11-i and j<=10):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("----------------------9th-------------------------")
for i in range(1,6):
    for j in range(1,11):
        if(j>=1 and j<=6-i or j>=5+i and j<=10):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("---------------------10th--------------------------")
for i in range(1,11):
    for j in range(1,11):
        if(j==i):
            print("\\",end=" ")
        if(j==11-i):
            print("/",end=" ")
        else:
            print("*",end=" ")
    print()
print("-----------------------11th------------------------")
for i in range(1,6):
    k=1
    for j in range(1,10):
        if(j>=6-i and j<=4+i and k):
            print("*",end="")
            k=0
        else:
            print(end=" ")
            k=1
    print()
print("----------------------6th-------------------------")
for i in range(1,6):
    k=1
    for j in range(1,10):
        if(j>=i and j<=10-i and k):
            print("*",end="")
            k=0
        else:
            print(end=" ")
            k=1
    print()
print("-----------------------12th------------------------")
for i in range(1,6):
    k=1
    for j in range(1,10):
        if(j>=6-i and j<=4+i and k):
            print("*",end="")
            k=0
        else:
            print(end=" ")
            k=1
    print()
for i in range(1,6):
    k=1
    for j in range(1,10):
        if(j>=i and j<=10-i and k):
            print("*",end="")
            k=0
        else:
            print(end=" ")
            k=1
    print()
print("----------------------13th-------------------------")
for i in range(1,8):
    for j in range(1,14):
        if(j>=8-i and j<=8-i or j>=6+i and j<=6+i):
            print("*",end="")
        else:
            print(end=" ")
    print()
for i in range(1,8):
    for j in range(1,14):
        if(j>=i and j<=i or j>=14-i and j<=14-i):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("----------------------14th-------------------------")
print(" ###################")
for i in range(13):
    for j in range(20):
        if(j==1 or j==19):
            print("#",end="")
        else:
            print(end=" ")
    print()
print(" ###################")
print()
print("------------------------15th----------------------")
for i in range(1,9):
          for j in range(1,29):
                    if((j>=8-i and j<=5+i)or(j>=22-i and j<=19+i)):
                              print("*",end="")
                    else:
                              print(end=" ")
          print()
for i in range(1,17):
          for j in range(1,29):
                    if((j>=i and j<=28-i)):
                              print("*",end="")
                    else:
                              print(end=" ")
          print()


