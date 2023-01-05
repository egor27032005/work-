#print("введите фамилию педагога: ")
#sername=input()
def shorting(sername):
    file=open('sernameTeachers.txt', 'r')
    liness = [] 
    with open ('sernameTeachers.txt', 'rt') as myfile:
        for myline in myfile: 
            liness.append(myline)
        #for j in range(3):
            if sername in liness:
                return print(sername) 
#shorting(sername) 