# Python quiz game

questions = ("How many elements are there in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "Which is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are there in the human body?: ",
             "Which plannet in the solar system is the hottest?: "
             )

options= (("A. 117", "B. 118", "C. 119", "D. 120"),
          ("A. Whale", "B. Crocodile", "C. ostrich", "D. chicken"),
          ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
          ("A. 206", "B. 207", "C. 208", "D. 306"),
          ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("B", "C", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, or D  ): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct! You got it!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1
print("--------------------------------------------")
print("                  RESULTS                   ")
print("--------------------------------------------")
print(f"Your score is {score} / {len(questions)}")