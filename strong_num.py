def is_strong(n:int)-> bool:
    sum=0
    temp = n
    while temp>0:
        sum=sum + (temp%10)**3
        temp = temp//10
    if n==sum:
        return True
    else:
        return False
    
def main():
   num=int(input("Enter an integer:"))
   if is_strong(num)==True:
       print("The number is strong")
   else:
       print("The number is not strong")
       
if __name__=="__main__":
    main() 