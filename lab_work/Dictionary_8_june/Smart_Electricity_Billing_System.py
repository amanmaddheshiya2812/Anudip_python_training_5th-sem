"""Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
         o Low Consumption (< 200)  
         o Medium Consumption (200–400)  
         o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300). """
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}
#-----------------------------------------------
# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house)
#-----------------------------------------------
# 2. Find the highest-consuming house
highest_house = max(units, key=units.get)
print(f"\nHighest Consumption:\n{highest_house} ({units[highest_house]} units)")
#-----------------------------------------------
# 3. Find the lowest-consuming house
lowest_house = min(units, key=units.get)
print(f"\nLowest Consumption:\n{lowest_house} ({units[lowest_house]} units)")
#-----------------------------------------------
# 4. Calculate total units consumed
total_units = sum(units.values())
print(f"\nTotal Units Consumed: {total_units}")
#-----------------------------------------------
# 5. Create lists based on consumption levels
low, medium, high = [], [], []
for house, consumption in units.items():
    if consumption < 200:
        low.append(house)
    elif 200 <= consumption <= 400:
        medium.append(house)
    else:
        high.append(house)
print(f"\nLow Consumption:\n{low}")
print(f"Medium Consumption:\n{medium}")
print(f"High Consumption:\n{high}")
#-----------------------------------------------
# 6. Count houses eligible for energy-saving campaign (> 300)
eligible_count = len([h for h in units.values() if h > 300])
print(f"\nEligible for Energy-Saving Campaign: {eligible_count}")