#print("введите фамилию: ")
#sername=input()
def short(sername):
    lines = [] 
    with open ('sernameStudents.txt', 'rt') as myfile:
        for myline in myfile: 
            lines.append(myline)
        #for j in range(3):
            if sername in lines:
                return print(sername) 
#short(sername)                      