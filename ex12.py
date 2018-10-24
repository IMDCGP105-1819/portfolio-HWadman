
cost_per_night = 70

def hotel_cost(nights):
    return nights * cost_per_night

def plane_ticket_cost(city, _class):
    if city == "New York":
        return 2000 * _class
    if city == "Auckland":
        return 790 * _class
    if city == "Venice":
        return 154 * _class
    if city == "Glasgow":
        return 65 * _class
    print("City not found!")
    return

def rental_car_cost(days):
    total = 0
    if days > 7:
        total -= 50
    elif days > 3:
        total -= 30
    total += (30 * days)
    if total < 0:
        total = 0
    return total

def total_cost(city, days, _class):
    total = 0
    total += hotel_cost(days-1)
    total += plane_ticket_cost(city,_class)
    total += rental_car_cost(days)
    print(f"The total cost of your holiday is £{total}")

total_cost(str(input("What city are you flying to? ")),int(input("How many days will you be there? ")),float(input("What class will you be flying? ")))
