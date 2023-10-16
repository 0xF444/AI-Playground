import math
departure = input("Please enter your departure time in this format: hh:mm\n")
arrival = input("Please enter your arrival time in this format: hh:mm\n")
hh_depar = int(departure[0:2])
mm_depar = int(departure[3:])
hh_arriv = int(arrival[0:2])
mm_arriv = int(arrival[3:])
depar_in_minutes = hh_depar * 60 + mm_depar
arriv_in_minutes = hh_arriv * 60 + mm_arriv

# Calculate the difference
difference = arriv_in_minutes - depar_in_minutes

# If negative, add 24 hours (1440 minutes) to account for day change
if difference < 0:
    difference += 1440

    # Convert back to hh:mm format
hh_diff = difference // 60
mm_diff = difference % 60

print(f"The trip time is equal to {abs(hh_diff)} hr and {abs(mm_diff)} min.")
