print("Round to the nearest hundredth on all questions.")

# Unit 1
pro1 = False
while not pro1:
    problem1 = input("\nRiddle me this, Batman! If an object starts at rest and accelerates at 2 m/s in 1.2 seconds, what is the final position of the object? ")
    if problem1 == "1.44":
        print("\nBruuuuuuuuuuuuuuuuuuce Waaaaaaaaaaaaaaaaaaaayne... You are correct! To solve this problem, we need to use the equation x = x0 + vx0*t + (1/2)*ax*t^2. The initial position is 0 meters and the initial velocity is zero, which means that the initial position and initial velocity are 0 in this case, leaving x = (1/2)*ax*t^2. Plugging in the acceleration (2 m/s) and the time (1.2 s) that we're given, your final answer should be 1.44 meters.")
        pro1 = True
    else:
        print("\nNO, you answered wrong Dark Knight! Here is a little hint: Use x = x0 + vx0*t + (1/2)*ax*t^2")
        print("")

# Unit 3
print("------------------------------------------------------------------")
pro2 = False
while not pro2:
    problem2 = input("\nRIDDDLEEEE ME THIS, BATMAN!!! What is the magnitude of the gravitational force of Mars on a 80 kg astronaut in a 127 kg space suit? The mass of Mars is 6.39 × 10^23 kg and the radius is about 3,400,000 meters and the gravitational constant is 6.67*10^-11 Nm^2/kg^2. ")
    if problem2 == "763.20":
        print("\nCorrect!!! That riddle was easy, BATMAN!! But I didn't think you'd be able to figure out that you have to use G*m1*m2/r^2 in order to find the gravitational force of Mars on the astronaut!!!")
        pro2 = True
    else:
        print("\nWRONG, WRONG, WRONG!!! Do you need a HINT?? I'll give you a hint, otherwise you will NEVER figure this out... Are you using G*m1*m2/r^2???? Did you add the mass of the astronaut and his suit together???")

# Unit 4
print("------------------------------------------------------------------")
pro3 = False
while not pro3:
    problem3 = input("\nRiddle me THIS, Batman! On a roller coaster, point A is the top of the roller coaster 50 meters high, point B is at the very bottom right after the drop, and point C is at the very top of the loop with HALF the height of point A. What is the velocity of the cart at point C, BATMAN???? ")
    if problem3 == "22.14":
        print("\nHeh... congratulations Batman... you answered RIGHT! You must have figured out that you need to set the gravitational potential energy at point A equal to the kinetic energy at point C plus the gravitational potential energy at point C, canceled the masses, and solved for velocity at point C(Good thing you remembered that the height at point C is half the height at point A, you must be a genius)!!! Curse you, BATMAN!!! You won't get my NEXT riddle correct!")
        pro3 = True
    else:
        print("\nABSOLUTELY WRONG, BATMAN! Try again! Here's a hint for you: The masses cancel out!")

# Unit 7
print("------------------------------------------------------------------")
pro4 = False
pro4a = False
while not pro4:
    problem4 = input("\nRIDDLEEEE ME THIS, BATS!!! A balling ball with a diameter of .22 meters rolls counterclockwise completing 325 revolutions per minute. What is the angular velocity of the bowling ball? ")
    if problem4 == "34.05":
        pro4 = True
        print("\nCORRECT!!! How did you do that??? Maybe because it was too EASYYY, you are not done with this problem yet! There is a SECOND PART!!!")
        while not pro4a:
            problem4a = input("\nWhat is the LINEAR velocity of the bowling ball, BATMAN??? ")
            if problem4a == "3.75":
                print("\nCORRECT!!! BUT HOW??? How did you know to first convert 325 rpm to revolutions per second to get 5.42 revolutions per second, then multiply it by 2pi to convert it to radians and plug that into angular velocity divided by the time to get an answer of 34.05 rads/s??? And how did you know the formula for linear velocity is v = ωr and all you had to do was divide the diameter by 2, plug in the angular velocity, and multiply it by the radius to get 3.75 m/s???")
                pro4a = True
                insult = input("\nType what you would like to say to the Riddler. Brag about winning, call him a loser or something. ")
                print("\nYou:", insult)
                print("\nRiddler: NO, NO, NO, NOOOO!!! This was NOT how it was supposed to GO!!! AAAAGHHH!!!")
                print("\nYou have beat the Riddler! Congratulations!")
            else:
                print("\nWRONGGGG!!! There is literally a simple formula for this, BATS, how could you get this WRONG!!!")
    else:
        print("\nWRONGGGGG!!!! TRY AGAIN!!!")
