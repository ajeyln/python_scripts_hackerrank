# To Georgien Leap Year
def is_leap(year):
    # Write your logic here
    if year % 400 == 0 :
        print("You have Entered Leap Year")
    elif year % 100 !=0 and year % 4 ==0:
        print("You have Entered Leap Year")
    else:
       print("Entered Year is not Leap year")

if __name__ == "__main__":
    year = int(input("Enter Year:"))
    is_leap(year)