"""Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).   
6. Count cities with temperature between 35°C and 40°C.  """
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}
#-----------------------------------------------
# 1. Display cities having temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
#-----------------------------------------------
# 2 & 3. Find the hottest and coolest city
hottest_city = max(temperature, key=temperature.get)
coolest_city = min(temperature, key=temperature.get)
print(f"\nHottest City: {hottest_city} ({temperature[hottest_city]}°C)")
print(f"Coolest City: {coolest_city} ({temperature[coolest_city]}°C)")
#------------------------------------------------
# 4. Calculate average temperature
avg_temp = sum(temperature.values()) / len(temperature)
print(f"\nAverage Temperature: {avg_temp:.1f}°C")
#------------------------------------------------
# 5. Create a list of pleasant cities (temperature < 35°C)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]
print(f"\nPleasant Cities:\n{pleasant_cities}")
#-----------------------------------------------
# 6. Count cities with temperature between 35°C and 40°C
# Note: Interpreted as inclusive [35, 40] to match sample output count of 4
count_between = len([temp for temp in temperature.values() if 35 <= temp <= 40])
print(f"\nCities Between 35°C and 40°C: {count_between}")