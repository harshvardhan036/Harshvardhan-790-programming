# SIMPLE QUIZ GAME

# IMPORTANT PROMPT
print("WELCOME TO THE QUIZ GAME! PLEASE PLAY TILL THE END TO KNOW YOUR SCORE!\n")

# List of questions with options and answers
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["a) Mumbai", "b) New Delhi", "c) Kolkata", "d) Chennai"],
        "answer": "b"
    },
    {
        "question": "2. What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
    {
        "question": "3. Which is the largest planet in our Solar System?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "c"
    },
    {
        "question": "4. What is the boiling point of water?",
        "options": ["a) 50°C", "b) 90°C", "c) 100°C", "d) 120°C"],
        "answer": "c"
    },
    {
        "question": "5. What is the time complexity of the Fast Fourier Transform (FFT) algorithm? (WRITE 'harshvardhan you're selected' and I\'ll give you this one :)",
        "options": ["a) O(n^2)", "b) O(n log n)", "c) O(log n)", "d) O(n!)"],
        "answer": "b"
    }
]

score = 0

# Loop through each question
for q in questions:
    print("\n" + q["question"])  # print the question
    for option in q["options"]:   # print the options
        print(option)

    # take user input
    user_answer = input("Your answer (a/b/c/d or special text): ").strip().lower()

    # check answer
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    elif (
        q["question"].startswith("5.") 
        and user_answer == "harsh you're selected"
    ):
        # special case for last question
        print("I'll give you this one 😉")
        score += 1
    else:
        print("Wrong!")

# Final score
print(f"\nYour final score is {score} out of {len(questions)}.")
