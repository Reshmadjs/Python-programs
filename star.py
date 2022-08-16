def star(n):
	star_count=0
	no_of_lines=1
	while(no_of_lines<n):
		if(star_count<no_of_lines):
			print("*", end=" ")
			star_count+=1
			continue

		if(star_count==no_of_lines):
			print("")
			star_count=0
			no_of_lines+=1
star(7)

