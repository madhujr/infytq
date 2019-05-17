strong_num_list=[]
def factorial(number):
    fact=1
    while number>=1:
        fact=fact*number
        number=number-1
    return(fact)


def find_strong_numbers(num_list):
    for i in range(0,len(num_list)):
        def digit_sum(x):
            r=0
            sum1=0
            while x!=0:
               r=x%10
               sum1=sum1+factorial(r)
               x=x//10
            return sum1
        num=num_list[i]
        res=digit_sum(num)
        if res==num:
            strong_num_list.append(num)

    return(strong_num_list)



num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
