schools = {
    "geometry": {
        "coordinates": [
            -81.50572799999999, 
            39.21675500000001
        ], 
        "type": "Point"
    }, 
    "properties": {
        "address": "300 Campus Drive, Parkersburg, WV 26104", 
        "marker-color": "#3F3040", 
        "marker-symbol": "circle", 
        "name": "West Virginia University at Parkersburg"
    }, 
    "type": "Feature"
}

# Example Question: How could you "slice" the dictionary to print "Feature" from line 15?
# Answer: print schools["type"]

# Question 1: What slice will give you a dictionary 
#   with the key of "coordinates" and a value containing a list
#   of two decimal numbers?

coordinatesDictionary = schools["geometry"]
print(coordinatesDictionary)

# Question 2: What slice will give you the address of the school?

schoolAddress = schools["properties"]["address"]
print(schoolAddress)

# Question 3: What slice will give you the name of the school?

schoolAddress = schools["properties"]["name"]
print(schoolAddress)

# Question 4: What slice will give you the latitude of the school? 
#   (Hint: the latitude is 39.216...)

schoolLat = schools["geometry"]["coordinates"][1]
print(schoolLat)

# Question 5 (bonus): What slice will give you the marker-color 
#   without the hashtag in front?

markerColor = schools["properties"]["marker-color"].slice(1)
print(markerColor)

