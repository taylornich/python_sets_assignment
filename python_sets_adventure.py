our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# question 1 task 1 #1

common_routes = our_routes.intersection(competitor_routes)

print(f"Both airlines fly to {common_routes}.")

# question 1 task 1 #2 

unique_routes = our_routes.difference(competitor_routes)

print(f"Destinations unique to our airline are {unique_routes}")

# question 1 task 1 #3

routes_not_shared = our_routes.symmetric_difference(competitor_routes)

print(f"Destinations not shared be either airline: {routes_not_shared}.")