  

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
  user_level_choice = input('So lets start from level 1. Type level 1:\n')
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
    level_2 = input("You have reached level 2, do you wish to continue or exit?\n")
    if level_2 == "continue" or level_2 == "yes":
      print ('have 2 free points for keeping up\n!')
      score += 2
      print ('your score is {}\n\n'.format(score))  

 
    level_2 = input("You have reached level 2, do you wish to continue or exit?\n")
    if level_2 == "continue" or level_2 == "yes":
      print ('have 2 free points for keeping up\n!')
      score += 2
      print ('your score is {}\n\n'.format(score))  

 
      print("Question 6: What is the Smallest Country in Asia?\n")
      print("a: Singapore")
      print("b: Maldives")
 
      response = input("What is your answer to this question?\n")
      if response == "b":
        print("Correct, way to go")
        score += 2
      else:
        print("sorry, not bad")
      score -= 1
      print("your score is {}\n".format(score))
 
 
 
      print("Question 7: Biggest Country in Asia?\n")
      print("a: China ")
      print("b: India ")
      print("c: Indonesia ")
 
      response = input("What is your answer to this question?\n")
      if response == "a":
        print("Correct, nice job here have a point")
        score += 2
      else:
        print("sorry, next time")
      score -= 1
      print("your score is {}\n".format(score))
 
 
      print("Question 8: Where is the Capital of Asia located?\n")
      print("a:  Seoul.")
      print("b:  Beijing.")
      print("c:  Tokyo.")
   
     
      response = input("What is your answer to this question?")
      if response == "b":
        print("Correct, don't stop!")
        score += 2
      else:
        print("sorry, but next time")
      score -= 1
      print("your score is {}\n".format(score))
 
      print("Question 9: How many states are there in Asia?\n")
      print("a: 49")
      print("b: 34")
      print("c: 57")
     
 
      response = input("What is your answer to this question?\n")
      if response == "a" or response == "b":
        print("Correct, nice job here have a point")
        score += 2
      else:
        print("sorry, next time")
      score -= 1
      print("your score is {}\n".format(score))
 
 
      print("Question 10: How many languages in Asia?\n")
      print("a: 2000 ")
      print("b: 3000")
      print("c: 2300")
      print("d:  1500")
 
      response = input("What is your answer to this question?\n")
      if response == "c":
        print("Correct, nice job here have a point\n\n")
        score += 2
      else:
        print("sorry, next time\n")
      score -= 1
      print('your score is {}'.format(score))
     
      if score>8:
        print('Wow amazing performance try this bonus question!\n\n')
 
      if score>8 :
        print('Bonus Question: Richest Country in Asia?')
        print('a: Korea')
        print("b: Singapore")
        print("c: China")
        print("d: Japan\n")
 
      if score>8 :
        response = input("What is your answer to this question?\n")
      if response == "c":
        print("Out-standing performance keep it up!\n")
        score += 2
      else:
        print("No worries no one's perfect but we can be perfect\n")
      score -= 1
      print("your Final score is {}!\n\n".format(score))
       
      print("THANKS FOR PLAYING!")
 
      PLAYERS_FEEDBACK = input(" Please rate this quiz out of ten and tell us what we could improve on \n")
 
      play_again = input("Do you want to restart? Yes or No\n")
 
      if play_again == "Yes" or play_again == "yes":
          exec(open("./Python quiz by Tanish.py").read())
      else:
          exit()
 
 
      print("Great choice\n\n")
    else:
      quit()
 
     
    