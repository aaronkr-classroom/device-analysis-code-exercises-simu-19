# main.py

from lib.room_sensor import RoomSensor

# Create 3 objects
sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 18, 35, 150)

# Store in list
sensors = [sensor1, sensor2, sensor3]

# Counters (Bonus)
comfortable = 0
normal = 0
warning = 0

# Loop
for s in sensors:
    s.show_info()
    
    level = s.comfort_level()
    print(f"Comfort Level: {level}")
    
    light = s.light_status()
    print(f"Light Status: {light}")
    print("-------------------")

    # Count categories
    if level == "Comfortable":
        comfortable += 1
    elif level == "Normal":
        normal += 1
    elif level == "Warning":
        warning += 1

# Final count
print(f"Comfortable: {comfortable}")
print(f"Normal: {normal}")
print(f"Warning: {warning}")