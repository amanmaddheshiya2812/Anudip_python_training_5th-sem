water_level = 0
fill_rate = 10
capacity = 100

while water_level < capacity:
    water_level += fill_rate
    print(f"Water Level: {water_level} liters")

print("\nTank is full.")