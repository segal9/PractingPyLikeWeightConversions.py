# python Quiz game
# with 5 questions
# use of a tuple here
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: " )

options = ( ("a. 116", "b. 117", "c. 118", "d. 119"),
            ("a. Whale", "b. Crocodile", "c. Elephant", "d. Ostrich"), 
            ("a. Nitrogen", "b. Oxygen", "c. Carbon-Dioxide", "d. Hydrogen"),
            ("a. 206", "b. 207", "c. 208", "d. 209"),
            ("a. Mercury", "b. Venus", "c. Earth", "d. Mars") )

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("???????????????????????????????????????????")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper() # the upper func makes it upper case
    guesses.append(guess) # adds it to the guess
    if guess == answers[question_num]:
        score += 1
        print("right on!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} is the right answer!")
    question_num += 1 # this displayed each option for each question

print("????????????????????????????")
print("          Results           ")
print("????????????????????????????")

print("answers: ", end="")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()

score = int( score / len(questions)*100 )
print(f"\nYour score is {score}%")