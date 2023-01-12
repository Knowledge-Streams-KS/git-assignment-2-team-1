#main file created

#func to divide two numbers 
def div(x,y):
  result=x/y
  print(x,"/",y,"=",result)
n1=int(input("enter the first number:"))  
n2=int(input("enter the second number:"))  
#func call
div(n1,n2)


#func to add two numbers 
def add(x,y):
  result=x+y
  print(x,"+",y,"=",result)
n1=int(input("enter the first number:"))  
n2=int(input("enter the second number:"))  
#func call
add(2,3)

#func to subtract two numbers 
def sub(x,y):
  result=x-y
  print(x,"-",y,"=",result)
n1=int(input("enter the first number:"))  
n2=int(input("enter the second number:"))  
#func call
sub(n1,n2)

#square root of a number
import math
num = float(input(" Enter a number: "))
sqRoot = math.pow(num, 0.5)
print("The square root of a given number {0} = {1}".format(num, sqRoot))
