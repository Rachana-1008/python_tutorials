def take_quiz():
    questions = [
        "What is the capital of France?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the largest planet in our solar system?",
        "In which year did the Titanic sink?",
        "Who is the famous physicist known for his theory of relativity?",
        "What is the capital of Japan?",
        "Which planet is known as the 'Red Planet'?",
        "Who painted the Mona Lisa?",
        "What is the powerhouse of the cell?",
        "Which ocean is the largest by surface area?"
    ]

    options = [
        ["a. Berlin", "b. Paris", "c. Rome", "d. Madrid"],
        ["a. Charles Dickens", "b. William Shakespeare", "c. Jane Austen", "d. Mark Twain"],
        ["a. Earth", "b. Jupiter", "c. Mars", "d. Saturn"],
        ["a. 1905", "b. 1912", "c. 1920", "d. 1931"],
        ["a. Isaac Newton", "b. Albert Einstein", "c. Galileo Galilei", "d. Stephen Hawking"],
        ["a. Beijing", "b. Tokyo", "c. Seoul", "d. Bangkok"],
        ["a. Venus", "b. Mars", "c. Jupiter", "d. Mercury"],
        ["a. Vincent van Gogh", "b. Leonardo da Vinci", "c. Pablo Picasso", "d. Michelangelo"],
        ["a. Nucleus", "b. Mitochondria", "c. Ribosome", "d. Endoplasmic reticulum"],
        ["a. Atlantic Ocean", "b. Indian Ocean", "c. Southern Ocean", "d. Pacific Ocean"]
    ]

    correct_answers = ["b", "b", "b", "b", "b", "b", "b", "b", "b", "d"]

    score = 0

    for i in range(10):
        print(f"\nQuestion {i + 1}: {questions[i]}")
        for option in options[i]:
            print(option)

        user_answer = input("Your answer: ").lower()

        if user_answer == correct_answers[i]:
            print("Correct! You earned 10 points.")
            score += 10
        else:
            print(f"Wrong. The correct answer is {correct_answers[i].upper()}.")

    print("\nQuiz completed!")
    print(f"Your total score is: {score}/100")


if __name__ == "__main__":
    take_quiz()
