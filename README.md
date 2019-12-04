# RockPaperScissors
Rock paper scissors game written in Python

This game is one of the project assignments on Colt Steele's Python course.

Break down: 
We need to import the method randint to produce random integers.
We set the variables of human and computer to 0 and set the winning score to 3.

We then prompt the user to enter their choice with input(), and also make it all lowercase to avoid case-sensitive related mistakes.
The machine will then be assigned a random number.
With an if else statement, the user's choice will be checked against the machine's, and the whoever gets it right wil have their score increased by 1. Whoever gets to 3 first wins.

The while loop will loop until the user or machine's score reaches 3, then it will exit it and another if else statement will print who wins.

The user can stop the game by entering 'q'.
