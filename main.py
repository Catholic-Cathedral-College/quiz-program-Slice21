  

restart = 1


while restart == 1:
  #!/bin/python3
 
  # this is the while loop for the question asking the player if they are ready?
  i = 0
  # this is code below prints the introduction/title of the quiz/game
  print('Welcome your in Sly\'s quiz game.')
 
  # input code for the user's name
  user_name = input('What is your Name?')
 
  # code that prints instructions for completing the quiz
  print ('\nHi There ' + user_name + '! Lets\'s play a Question and Answer game or you could say a QUIZ!\n')
  print ('So you basically you have a question in front of you.\n\nYou have options and you write if it is (a,b,c, or d) not (A, B, C, or D)')

 
 
  # score initialization
  score = 0
 
  # asking the player if he/she is prepared to answer the questions
  while i<1:
    ready = input("Are You Ready? Type 'yes' or 'no'\n")
    if ready == 'yes' or ready == 'Yes':
      print('let\'s go then\n')
      i = 1
   
  # player's choice for difficulty
  user_level_choice = input('What level do you like to start from, Level 1 or Level 2. Type level 1 or level 2:\n')
  if user_level_choice == 'level 1':
    # Start of question 1
    print("Question 1: Which country has a red and blue Taegeuk in its center?\n")
    print("a: Japan")
    print("b: Korea")
    print("c: China")
    print("d: Philippines")
 
    # Code defining whether player's input is right or wrong for question 1 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, knowledge always pays off")
      score += 2
    else:
      print("sorry incorrect, don't worry many questions left to go!, try again")
    score -= 1
    print("your score is {}\n".format(score))
 
    # Start of question 2
 
    print("Question 2: What Country in Asia has highest population?\n")
    print("a: Philippines")
    print("b: China")
    print("c: Japan")
    print("d: Korea")
 
    # Code defining whether player's input is right or wrong for question 2 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, next time")
    score -= 1
    print("your score is {}\n".format(score))
 
    # Start of question 3
 
    print("Question 3: What Country in Asia has 7,641 islands?\n")
    print("a: Korea")
    print("b: Thailand")
    print("c: China")
    print("d: Philippines")
 
    # Code defining whether player's input is right or wrong for question 3 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "d":
      print("Correct, good job")
      score += 2
    else:
      print("sorry incorrect")
    score -= 1
    print("your score is {}\n".format(score))
 
    # Start of question 4
 
    print("Question 4: What Country makes a Ramen?")
    print("a: China")
    print("b: Korea")
    print("c: Japan")
    print("d: Taiwan")
 
    # Code defining whether player's input is right or wrong for question 4 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, for the loss of your points")
    score -= 1
    print("your score is {}\n".format(score))
 
 
    # Start of question 5
    
 
    print("Question 5: What is the Largest continent in the world?\n")
    print("a: Africa")
    print("b: North America")
    print("c: Asia")
    print("d: Antartica")

 # Code defining whether player's input is right or wrong for question 4 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, for the loss of your points")
    score -= 1
    print("CONGRATULATIONS YOUR SCORE IS {}\n".format(score))