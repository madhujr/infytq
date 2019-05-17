def generate_ticket(airline,source,destination,no_of_passengers):
  
    ticket_number_list=[]

    start=101

    temp=start

    end=no_of_passengers+start
 
   for i in range(temp,end):
 
       part2=source[0:3]

        part3=destination[0:3]

        ticket=airline+":"+part2+":"+part3+":"+str(temp)

        ticket_number_list.append(ticket)

        temp=temp+1
  
    return ticket_number_list[-5:]
    
