def find_winner_of_the_day(*match_tuple):
    count1=0
    count2=0
    n=len(match_tuple)
    for i in range(0,n):
        if match_tuple[i]=="Team1":
            count1=count1+1
        elif match_tuple[i]=="Team2":
            count2=count2+1
    if count1>count2:
        str1="Team1"
        return(str1)
    elif count1<count2:
        str2="Team2"
        return(str2)
    elif count2==count1:
        str3="Tie"
        return(str1)
    
    
    
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))



