# Calculate Rocket Fuel

def calculate_rocket_fuel_required(distance):
   fuel = distance * 15

   if fuel < 100: 
      return 100
   else:
      return fuel
   
#
##
###
####
   
# Calculate Circus Ticket Price

def calculate_ticket_price_for_performer(regular_ticket_price, performer_type):
    if performer_type == "Juggler":
        return regular_ticket_price * 0.5
    elif performer_type == "Fire Twirler":
        return regular_ticket_price * 0.75
    elif performer_type == "Magician":
        return regular_ticket_price * 0.20
    elif performer_type == "Escape Artist":
        return regular_ticket_price * 0
    else:
        return regular_ticket_price * 0.8