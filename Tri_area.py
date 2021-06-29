#function tri_area
def tri_area (base,height):
    return  (base * height) / 2
    
#Program
base = int (input ("Base of the triangle \n"))
height = int (input ("height of the triangle \n"))
print ("The area of the triangle is : \n ", tri_area (base,height))
