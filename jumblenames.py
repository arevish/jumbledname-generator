import random
numb = int(input("Enter number of names you want to input: "))
namelist = []
for i in range(numb):
    names = input("Enter names:  ")
    namelist.append(names)
print(namelist)
seprateName=[]
fistname = []
lastname = []
for i in namelist:
    seprateName = i.split(" ")
    # print(seprateName)
    fistname.append(seprateName[0])
    lastname.append(seprateName[1])
# print(fistname)
# print(lastname)
fun_names=[]
for i in range(numb):
    n= random.randint(0,numb)
    jumble = [fistname[i] +" " + lastname[n-1]]
    
    fun_names.append(jumble)
print(fun_names)