#Find the right set point for synchronised clocks.
#Made by TehKonnos
x=int(input("Enter Hz: "))
mc=4 #Machine cycles
dHz=48 #Default PIC18F4550 Hz setting
tmc=mc*(1/dHz*pow(10,3)) #Nanosec for 1 Machine Cycle. tmc=83,333nsec
nanosec=((1/x)/2)*pow(10,9) # Converting Hz to Nanosec
print("Nanosec of Hz =",nanosec,"nanoseconds")
print ("Time for 1 Machine Cycle=",tmc,"nanoseconds")
division=1
while(division<=256):
	den=tmc*division #Denominator
	fres=65536-(nanosec/den) #Float start point.
	if(fres>0):
		rres=(round(65536-(nanosec//den))) #Rounded 'fres' value
		if(rres==fres): #Change this into rres-fres<-0.5 if no values appear.
			print("---------------------")
			print("Tried with div: "+str(division)) #What you put at -> T0_DIV_X
			print ("Start point: "+str(rres)) #The value you should use
	division*=2
print("End of Program.")