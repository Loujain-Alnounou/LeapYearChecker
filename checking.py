

def leap_year_check(num):
    """
    checks if a year is a leap year or not 
    by checking the numbers divisibility 
    
    param:
    ----
    num= an integer that gets checked 
    
    return:
    ---
    none
    """
    if int(num) %400==0:
        print(num, "is a leap year")
    elif int(num) %100==0:
        print(num, "is not a leap year")
    elif int(num) %4==0:
        print(num, "is a leap year")
    else:
        print(num, "is not a leap year")
    
    
def main():
    """
    takes user input and checks if its valid or not, 
    if its valid the it runs the leap year checker function.
    
    param: none 
    
    return: none 
    """
    num= input("enter a year:")
    if num.isdigit():
        leap_year_check(num)
    else:
        print(" Error:invalid input")


    

    
if __name__== "__main__":
    main()
    
    
    
    
    