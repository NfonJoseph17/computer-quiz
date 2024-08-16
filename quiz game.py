print("Welcome to my advanced computer quiz!")

status = input("Are you ready to play the quiz? (y/n): ").lower()

if status != "y":
    print("Okay! See you next time!")
    quit()

print("Rules: Answer type T for 'True' and F for 'False'")

questions = {
    "A monitor displays information. ": "T",
    "An SD card is an output device. ": "F",
    "A microphone is an input device. ": "T",
    "A pen drive is a storage device. ": "T",
    "Microsoft Office is a piece of software. ": "T",
    "A firewall is a type of hardware. ": "F",
    "The CPU is referred to as the stomach of the computer. ": "F",
    "A computer is a piece of hardware. ": "T",
    "A terabyte is equal to 1 million gigabytes. ": "F",
    "CD stands for Collective Disk. ": "F",
}

score = 0
correct_questions = []
wrong_questions = []

for question, correct_answer in questions.items():
    answer = input(question).strip().upper()
    if answer == correct_answer:
        score += 1
        correct_questions.append(question)
        print("Correct!")
    else:
        wrong_questions.append(question)
        print("Incorrect.")

print(f"\nYour final score is {score}/{len(questions)}")

if score == len(questions):
    print("Congrats! You answered all questions correctly!")
elif score < (len(questions) / 2):
    print("You were not able to score half of the questions. Try again.")
else:
    print("You did great!")

print(f'\nCorrectly answered questions: {correct_questions}')
print(f'Questions you answered incorrectly: {wrong_questions}')