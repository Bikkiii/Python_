travel_log=[
        {"City":"Kathmandu","Places_visited":["Swayambhu", "Pashupati", "Basantpur"], 
         "total_visits": 20},
    
    {"City":"Lalitpur","places_visited":["Patan","Godawari","Satdobato"], 
    "total_visits": 25}
]

def add_new_city(city,no_of_visits,places_visited):
    new_city={}
    new_city["City"]= city
    new_city["total_visits"]=no_of_visits
    new_city["Places_visited"]=places_visited
    print(new_city)
    travel_log.append(new_city)
    # print(f"You've visited {city} {no_of_visits} Times")
    # print(f"You've been to {places_visited[0]}, {places_visied[1]} and {places_visited[2]}")
    


add_new_city(city="Bhaktapur",no_of_visits=5,places_visited=["Bhakatpur durbar square","Kamal Pokhari","Nagarkot"])
print(travel_log)