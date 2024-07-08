y=int(input("Enter Year for Leapyear Cheaking: "))
if((y % 4 == 0 and y % 100 != 0 or y % 400 == 0)):
   print("It's a Leap Year")
else:
   print("Not a Leap Year")