#program for display battery level
charging_level = 10
electricity_status = True
while(charging_level<=100):
    if(electricity_status):
        print("Battery level :",charging_level,"%")
        charging_level=charging_level+10
    else:
        break
print("Fully Charged")