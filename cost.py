def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost = cost - 50
  elif days >= 3:
    cost = cost - 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

%%% this is a test %%%
while True:
  a = int(input("nb of days: "))
  b = int(input("extra costs $: "))
  print (trip_cost("Los Angeles", a, b))
  if input("calculate again? :") == "no":
    break

