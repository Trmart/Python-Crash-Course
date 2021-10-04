# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed 
# for the appropriate color alien.

alien_color = "Yellow" 

if(alien_color.lower() == "green"):
    print("Player 1 earned 5 pts")

elif(alien_color.lower() == "yellow"):
    print("Player 1 earned 10 pts")

elif(alien_color.lower() == "red"):
    print("Player 1 earned 15 pts")
else:
    print("Player 1 earned 0 pts")