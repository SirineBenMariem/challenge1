#function list_of_multiples
def list_of_multiples(num,length):
    liste = []
    x = 0
    while (x != length):
        liste.append(num + (num * x))
        x = x + 1
    return liste

#the program
num = int (input ("The num is \n"))
length = int (input ("The length of the list is \n"))
print ("The list of multiples of ", num , "is : \n ", list_of_multiples(num,length))
