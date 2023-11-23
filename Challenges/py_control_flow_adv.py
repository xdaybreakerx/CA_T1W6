# Mission to Mars

def ready_to_embark_on_mission(have_supplies, distance_to_mission_site, fuel_in_vehicle):
    can_walk_to_mission_site = distance_to_mission_site <= 10
    if have_supplies and can_walk_to_mission_site:
        return True

    if have_supplies and (fuel_in_vehicle * 2) >= distance_to_mission_site:
        return True

    return False

  
#
##
###
####
   
# Cost of visiting cinema

def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):
    entry_ticket_cost = 15 if age < 60 else 10
    candy_cost = 10 if has_membership == False else 5
    parking_cost = 3 if transport_type == "Car" else 0

    return entry_ticket_cost + candy_cost + parking_cost

#
##
###
####