    #function countTrue
def countTrue(n,t):
    if (n == 0):
        return 0
    else :
        return t.count(1)

#the program
n = int (input ("the length of the array is \n"))
t = []
for i in range (n) :
    x = bool(input("write True of False \n"))
    if ((x == True) or (x == False )):
        t.append (x)
    else :
        t.append (False)

print ("The numbre of True elements is : \n", countTrue(n,t)) 
    
