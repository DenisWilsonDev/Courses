"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

def add_city_to_dict(dict, city, country, continent):
    if dict.has_key(continent):
        if dict[continent].has_key(country):
            dict[continent][country].append(city)
        else:
            dict[continent][country] = [city]
    else:
        dict[continent] = {country: [city]}
   
add_city_to_dict(locations, 'Bangalore', 'India', 'Asia')
add_city_to_dict(locations, 'Atlanta', 'USA', 'North America')
add_city_to_dict(locations, 'Cairo', 'Egypt', 'Africa')
add_city_to_dict(locations, 'Shanghai', 'China', 'Asia')


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

print 1
for city in sorted(locations['North America']['USA']):
    print city

print 2    
cities = []   
for country in locations['Asia']:
    for city in locations['Asia'][country]:
        cities.append(city + ' - ' + country)
for item in sorted(cities):
    print item