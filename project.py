import random



print("Welcome to the era :) ")
a=input("Do you want to play the game (y/n) : ").lower()
#scores
s1=0
s2=0
s3=0
s4=0
if a != 'y' :
	quit()

#questions
def question(x,p) :
	if x==1 :
		global s1
		global s2
		global s3
		q1=input("Which is the national animal of india ").lower()
		if q1=='tiger' :
			print("correct!!")
			if p==p1 :
				s1+=3
			elif p==p2 :
				s2+=3
			else :
				s3+=3

		else :
			print("INCORRECT***!")
			
	if x==2 :
		q2=input("Which is the national bird of india ").lower()
		if q2=='peacock' :
			print("correct!!")
			if p==p1 :
				s1+=3
			elif p==p2 :
				s2+=3
			else :
				s3+=3
		else :
			print("INCORRECT***!")
			
	if x==3 :
		q3=input("What’s the fastest land animal in the world? ").lower()
		if q3=='cheetah' :
			print("correct!!")
			if p==p1 :
				s1+=3
			elif p==p2 :
				s2+=3
			else :
				s3+=3
		else :
			print("INCORRECT***!")
			
	if x==4 :
		q4=input("Which is the longest river in the world ? ").lower()
		if q4=='nile' :
			print("correct!!")
			if p==p1 :
				s1+=3
			elif p==p2 :
				s2+=3
			else :
				s3+=3
		else :
			print("INCORRECT***!")
			
	if x==5 :
		q5=input("How many eyes does a bee have? (number only) ")
		if q5=='5' :
			print("correct!!")
			if p==p1 :
				s1+=3
			elif p==p2 :
				s2+=3
			else :
				s3+=3
		else :
			print("INCORRECT***!")
			
	if x==6 :
		q6=input("How many bones does a baby have? ")
		if q6=='300' :
			print("correct!!")
			if p==p1 :
				s1+=3
			elif p==p2 :
				s2+=3
			else :
				s3+=3
		else :
			print("INCORRECT***!")

def question2(x,p) :
		if x==1 :
			global s1
			global s2
			global s3
			q1=input("who won the first nobel prize in india? ").lower()
			if q1=='rabindranath tagore' :
				print("correct!!")
				if p==p1 :
					s1+=5
				elif p==p2 :
					s2+=5
				else :
					s3+=5

			else :
				print("INCORRECT***!")
				
		if x==2 :
			q2=input("Who invented Computer? ").lower()
			if q2=='charles babbage' :
				print("correct!!")
				if p==p1 :
					s1+=5
				elif p==p2 :
					s2+=5
				else :
					s3+=5
			else :
				print("INCORRECT***!")
				
		if x==3 :
			q3=input("which team has won more number of IPL TROPHIES? ").lower()
			if q3=='mumbai indians' :
				print("correct!!")
				if p==p1 :
					s1+=5
				elif p==p2 :
					s2+=5
				else :
					s3+=5
			else :
				print("INCORRECT***!")
				
		if x==4 :
			q4=input("The most expensive player in the IPL 2022 aucton? ").lower()
			if q4=='ishan kishan' :
				print("correct!!")
				if p==p1 :
					s1+=5
				elif p==p2 :
					s2+=5
				else :
					s3+=5
			else :
				print("INCORRECT***!")
				
		if x==5 :
			q5=input("What is the factorial of zero(0!): ")
			if q5=='1' :
				print("correct!!")
				if p==p1 :
					s1+=5
				elif p==p2 :
					s2+=5
				else :
					s3+=5
			else :
				print("INCORRECT***!")
				
		if x==6 :
			q6=input("Which is next leap year? ")
			if q6=='2024' :
				print("correct!!")
				if p==p1 :
					s1+=5
				elif p==p2 :
					s2+=5
				else :
					s3+=5
			else :
				print("INCORRECT***!")

def question3(x,p) :
		if x==1 :
			global s1
			global s2
			global s3
			q1=input("what is full form of BCCI in cricket? ").lower()
			if q1=='the board of control for cricket in india' :
				print("correct!!")
				if p==p1 :
					s1+=7
				elif p==p2 :
					s2+=7
				else :
					s3+=7

			else :
				print("INCORRECT***!")
				
		if x==2 :
			q2=input("Most electonegative element in the perodic table? ").lower()
			if q2=='fluorine' :
				print("correct!!")
				if p==p1 :
					s1+=7
				elif p==p2 :
					s2+=7
				else :
					s3+=7
			else :
				print("INCORRECT***!")
				
		if x==3 :
			q3=input("Who was known as Iron man of India? ").lower()
			if q3=='sardar vallabhai patel' :
				print("correct!!")
				if p==p1 :
					s1+=7
				elif p==p2 :
					s2+=7
				else :
					s3+=7
			else :
				print("INCORRECT***!")
				
		if x==4 :
			q4=input("ISRO Stands for? ").lower()
			if q4=='indian space research organisation' :
				print("correct!!")
				if p==p1 :
					s1+=7
				elif p==p2 :
					s2+=7
				else :
					s3+=7
			else :
				print("INCORRECT***!")
				
		if x==5 :
			q5=input("In baseball, how many players are there in one team? ")
			if q5=='9' :
				print("correct!!")
				if p==p1 :
					s1+=7
				elif p==p2 :
					s2+=7
				else :
					s3+=7
			else :
				print("INCORRECT***!")
				
		if x==6 :
			q6=input("what is the time span of a test match? ")
			if q6=='5' :
				print("correct!!")
				if p==p1 :
					s1+=7
				elif p==p2 :
					s2+=7
				else :
					s3+=7
			else :
				print("INCORRECT***!")

def question4(x,p) :
		if x==1 :
			global s1
			global s2
			global s3
			q1=input("The activity of a radioactive source has a unit measurement as? (A. Becquerel) (B. Jansky) (C. Dioptre)(D. Erlang) ").lower()
			if q1=='a' or "bacquerel" :
				print("correct!!")
				if p==p1 :
					s1+=10
				elif p==p2 :
					s2+=10
				else :
					s3+=10

			else :
				print("INCORRECT***!")
				
		if x==2 :
			q2=input("what is the scale to determine the acidity or basidity of a solution? ").lower()
			if q2=='ph scale' or "ph" :
				print("correct!!")
				if p==p1 :
					s1+=10
				elif p==p2 :
					s2+=10
				else :
					s3+=10
			else :
				print("INCORRECT***!")
				
		if x==3 :
			q3=input("what is the square root of -1? (A. 1) (B. -i) (C. -1) (D. non of the above) ").lower()
			if q3=='d' :
				print("correct!!")
				if p==p1 :
					s1+=10
				elif p==p2 :
					s2+=10
				else :
					s3+=10
			else :
				print("INCORRECT***!")
				
		if x==4 :
			q4=input("Name the metal at liquid at room temperature ? ").lower()
			if q4=='mercury' :
				print("correct!!")
				if p==p1 :
					s1+=10
				elif p==p2 :
					s2+=10
				else :
					s3+=10
			else :
				print("INCORRECT***!")
				
		if x==5 :
			q5=input("Which is the brightest planet on the night sky? ").lower()
			if q5=="venus" :
				print("correct!!")
				if p==p1 :
					s1+=10
				elif p==p2 :
					s2+=10
				else :
					s3+=10
			else :
				print("INCORRECT***!")
				
		if x==6 :
			q6=input("A score means how many years? ")
			if q6=='20' :
				print("correct!!")
				if p==p1 :
					s1+=10
				elif p==p2 :
					s2+=10
				else :
					s3+=10
			else :
				print("INCORRECT***!")
			
		
#Begining of the game************************************************
print("Let's start the game@ ")

participants=int(input("Enter the number of participants(*max:3) "))
if participants == 1 :
	p1=input("Enter the name of  participant ")
	choices=[1,2,3,4,5,6]
	roll_dice=random.choice(choices)

	#Round 1
	print("ROUND : 1")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("Your number is : ", roll_dice)
		question(roll_dice,p1)
		print('Your score is : ',s1)

	#ROUND 2
	print("ROUND : 2")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("Your number is : ", roll_dice)
		question2(roll_dice,p1)
		print('Your score is : ',s1)

	#ROUND 3
	print("ROUND : 3")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question3(roll_dice,p1)
		print('Your score is : ',s1)


	#Round4******************************
	print("ROUND : 4")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question4(roll_dice,p1)
		print('Your score is : ',s1)
	print("Your score is : ",s1)

#For p2
if participants == 2 :
	p1=input("Enter the name of first participant ")

	p2=input("Enter the name of second participant ")

	choices=[1,2,3,4,5,6]

	roll_dice=random.choice(choices)

	#Round 1
	print("ROUND : 1")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p2)
		print('Your score is : ',s2)
	
	#Round 2************************************************************
	print("ROUND : 2")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question2(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question2(roll_dice,p2)
		print('Your score is : ',s2)

	#Round 3*******************************************************
	print("ROUND : 3")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question3(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question3(roll_dice,p2)
		print('Your score is : ',s2)


	#Round4******************************
	print("ROUND : 4")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question4(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question4(roll_dice,p2)
		print('Your score is : ',s2)
	
	dic={s1:p1,s2:p2}
	x=max(dic)
	winner=dic.get(x)
	print("SO WINNER OF THE GAME IS ##!!: ",winner,end='')
	print("  WINNER WINNER CHICKEN DINNER")

#Paricipants 3

if participants == 3 :
	p1=input("Enter the name of first participant ")

	p2=input("Enter the name of second participant ")

	p3=input("Enter the name of third participant ")

	choices=[1,2,3,4,5,6]

	roll_dice=random.choice(choices)

	#Round 1
	print("ROUND : 1")
	#for p1
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)

	#for p2

	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p2)
		print('Your score is : ',s2)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)

	print(p3 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p3)
		print('Your score is : ',s3)
	
	#Round 2************************************************************
	print("ROUND : 2")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question2(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question2(roll_dice,p2)
		print('Your score is : ',s2)

	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)

	print(p3 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p3)
		print('Your score is : ',s3)

	#Round 3*******************************************************
	print("ROUND : 3")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question3(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question3(roll_dice,p2)
		print('Your score is : ',s2)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)

	print(p3 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p3)
		print('Your score is : ',s3)


	#Round4******************************
	print("ROUND : 4")
	print(p1 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question4(roll_dice,p1)
		print('Your score is : ',s1)
	
	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)
	print(p2 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question4(roll_dice,p2)
		print('Your score is : ',s2)

	choices.remove(roll_dice)	
	roll_dice=random.choice(choices)

	print(p3 , "Begine the game by rolling the dice ")
	c=input("press k to roll the dice ").lower() 
	
	if c == "k":
		print("You got " , "Your number is : ", roll_dice)
		question(roll_dice,p3)
		print('Your score is : ',s3)
	
	dic={s1:p1,s2:p2,s3:p3}
	x=max(dic)
	winner=dic.get(x)
	print("SO WINNER OF THE GAME IS ##!!: ",winner,end='')
	print("  WINNER WINNER CHICKEN DINNER")


