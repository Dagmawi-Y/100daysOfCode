# student = {
#     'name': 'Dag',
#     'age': 23,
#     'grade': 'A'
# }



# for i in student:
#     # print(i)
#     print(student[i])

# Nesting dict inside a dict
travel_log = {
    "Ethiopia" : {
        "cities_visited":["Addis", "Hawassa", "Axum"],
        "total_visits": 12
        },
    "USA": ["DC", "Boson", "California"]
},

# Nesting a dict inside a list

travel_log = [
    {
        "Country": "Ethiopia",
        "cities_visited":["Addis", "Hawassa", "Axum"],
        "total_visits": 12
    },
    {
        "Country": "Ethiopia",
        "cities_visited":["Addis", "Hawassa", "Axum"],
        "total_visits": 12
    }
]

print(travel_log[0])