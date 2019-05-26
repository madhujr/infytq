def check_double(number):
   double=2*number
   a=str(number)
   b=str(double)
   c=len(a)
   d=len(b)
   if c==d:
       if sorted(str(a))==sorted(str(b)):
           return(True)
       else:
           return(False)
   else:
       return(False)
   

print(check_double(9))
