 {questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A: Paris", "B: London", "C: Berlin", "D: Madrid"],
        "answer": "A"
    },
     {
        "question": "What is the capital of Sweden?",
        "options": ["A: Dubai", "B: London", "C: Berlin", "D: Stockholm"],
        "answer": "D"
    },
     {
        "question": "What is the capital of Aghanistan?",
        "options": ["A: Tokyo", "B:Kabul", "C: Berlin", "D: Ottawa"],
        "answer": "B"
    },
     {
        "question": "In which year was Microsoft founded ?",
        "options": ["A: 1975", "B: 1985", "C: 1995", "D:2005"],
        "answer": "A"
    },
     {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A: Tomato", "B: Avocado", "C: Lime", "D: Onion"],
        "answer": "B"
    },
     {
        "question": "Who wrote the book Mio My Son?",
        "options": ["A: Astid Lindgren", "B: Roald Dahl", "C: J.K Rowling", "D: Enid Blyton"],
        "answer": "A"
    },
     {
        "question": "What is the capital of France?",
        "options": ["A: Sydney", "B: Canberra", "C: Berlin", "D: Madrid"],
        "answer": "B"
    },
     {
        "question": "Which country oroduces the most coffe in the world?",
        "options": ["A: Brezil", "B: Colombia", "C: Vietnam", "D: Ethiopia"],
        "answer": "A"
    },
     {
        "question": "Which planet is the closest the sun?",
        "options": ["A: Mars", "B: Venus", "C: Jupiter", "D: Mercury"],
        "answer": "D"
    },
     {
        "question": "Which animal is the largest species on Earth?",
        "options": ["A: Seal", "B: Elephant", "C:  Blue whale", "D: Tiger"],
        "answer": "C"
    },

]
# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")
    run_quiz(questions)