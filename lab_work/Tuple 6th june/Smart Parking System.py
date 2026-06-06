slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Count occupied and available slots
occupied_count = slots.count(1)
available_count = slots.count(0)

# Find the first available slot (using 0-based indexing)
first_available = slots.index(0)

# Display all available slot numbers
# Using 1-based indexing for "slot numbers" commonly used in parking
available_slots = [i + 1 for i, status in enumerate(slots) if status == 0]

# Check whether parking occupancy exceeds 75%
occupancy_rate = (occupied_count / len(slots)) * 100
exceeds_threshold = occupancy_rate > 75

# Output Results
print(f"Occupied: {occupied_count}, Available: {available_count}")
print(f"First available slot index: {first_available}")
print(f"Available slot numbers: {available_slots}")
print(f"Occupancy exceeds 75%? {'Yes' if exceeds_threshold else 'No'} ({occupancy_rate}%)")