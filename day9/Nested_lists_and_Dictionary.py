#Nesting Nesting
# {key1: Value,
# key2: value,
# key3: list[]      #list
# key4: {dict}}   #dictionary

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a list in a dictionary

travel_log={
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}
# print(travel_log["France"])

#Nesting Dictionary in a Dictionary
# travel_log={
#     "France":{"Cities_visited": ["Paris","Lille","Dijon"], "total_visits":5},
#     "Germany": ["Berlin","Hamburg","Stuttgart"]
# }
# print(travel_log["France"])

travel_log={
    "Kathmandu": 
        {"Places_visited":["Swayambhu", "Pashupati", "Basantpur"], 
         "total_visits": 20},
    "Lalitpur": 
    {"places_visited":["Patan","Godawari","Satdobato"], 
    "total_visits": 25}
    }
# print(travel_log["Lalitpur"])

#Nesting a dictionary inside a list

# [{
#     key1:[List],
#     key2:{Dict}
# },
#  {
#      key1:value,
#      key2:value,
#  }]

travel_log=[
        {"City":"Kathmandu","Places_visited":["Swayambhu", "Pashupati", "Basantpur"], 
         "total_visits": 20},
    
    {"City":"Lalitpur","places_visited":["Patan","Godawari","Satdobato"], 
    "total_visits": 25}
]
print(travel_log[0])