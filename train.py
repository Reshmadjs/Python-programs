# A train leaves station A at 4.00 a.m and travels at 80kmph. After every 30 minutes, it reaches
# a station where it halts for 10 minutes. It reaches its final destination B at 1.00 p.m. Display a
# table showing its arrival and departure time at every intermediate station. Also calculate the total
# distance between A and B.

def add_minutes_in_time(hour, minutes, add_minute):
	if ((minutes+add_minute) >= 60):
		hour += 1
		minutes = (minutes+add_minute) - 60
	else:
		minutes += add_minute
	return hour,minutes

departure_hour = 4
departure_minutes = 00


print("Arrival  |   departure ")
print(" NA      |   {}:{}".format(departure_hour, departure_minutes))
count = 0
while True:
	arrival_hour, arrival_minutes = add_minutes_in_time(departure_hour,departure_minutes,30)
	departure_hour, departure_minutes = add_minutes_in_time(arrival_hour,arrival_minutes,10)
	print("{}:{}     |   {}:{}".format(arrival_hour, arrival_minutes, departure_hour, departure_minutes))
	count +=1
	
	if (departure_hour > 12):
		break;

print("Total distance: {} KM	".format((40*count)))








