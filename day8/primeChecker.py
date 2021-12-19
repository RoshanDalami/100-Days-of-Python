#Write your code below this line 👇
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.



#Write your code above this line 👆
    
#Do NOT change any of the code below👇

n = int(input("Check this number: "))

def prime_checker(n):
    prime = False
    for i in range(2,n):
        if n%i == 0 :
            prime = True

            
    if(prime):
        print("It's not a prime number.")  
    else:
        print("It's is a prime number.")              
                
            
prime_checker(n)
