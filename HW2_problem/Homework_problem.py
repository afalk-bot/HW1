"""
Hosting at a restauraunt
Determining wait times based on party size, table preference, and reservations
"""

has_reservation=input("Does the party have a reservation?")
party_size=int(input("How many people are in the party?"))
booth_requested=input("Did they request a booth?")
high_top=input("Are they willing to be at a high top?")
all_arrived=input("Is everyone here?")

def restaurant_seating(has_reservation,party_size,booth_requested,high_top,all_arrived):
    if party_size<=0 or party_size>20:
        return "Invalid party size"
    elif has_reservation != "yes" and has_reservation != "no":
        return "Invalid reservation response"
    elif booth_requested!= "yes" and booth_requested != "no":
        return "Invalid booth response"
    elif high_top!= "yes" and high_top!= "no":
        return "Invalid high top response"
    elif all_arrived != "yes" and all_arrived != "no":
        return "Invalid arrival input"
    
    elif has_reservation=="yes" and all_arrived=="yes":
        response= "The party can be seated immediately"
    elif has_reservation=="yes" and all_arrived=="no":
        response="The party must wait until all members have arrived"
    elif party_size>4:
        response= "There will be a 30 minute wait"
    elif party_size<=4 and booth_requested=="yes":
        response="It will be an hour wait"
    elif party_size<=4 and high_top=="yes":
        response= "The party can be seated immediately"
    elif party_size<=4 and high_top=="no" and booth_requested=="no":
        response="It will be a 20 minute wait."
    
    return response

seating=restaurant_seating(has_reservation,party_size,booth_requested,high_top,all_arrived)
print(seating)

    
