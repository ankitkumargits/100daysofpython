print("Sets methods in python")

cities = {"Jaipur", "Jodhpur", "Ajmer"}
print(cities)
cities2 = {"Bikaner", "Udaipur", "Jaisalmer", "Jaipur"}
city = cities.union(cities2)
city2 = cities.intersection(cities2)  # you can insection update values here
city3 = cities.update(cities2)  # symmertic diffrence between sets
print(cities)    # diffrence between sets 
# isdisjoint sets are given true or false
# isupperset 
# issubset 
cities.add("Helansiki")
# cities.remove("Jaipur") # it gives an error
# cities.discard("Jaipur") # it can't be given an error
# item = cities.pop() # it remove from random index in set
# print(item)
# print(cities)
# del cities  # it can delete a set in python 
cities.clear()
print(cities)