import random

questions = [
    {
        "question": "What is the capital city of Kenya?",
        "choices": {"A": "Accra", "B": "Kigali", "C": "Nairobi", "D": "Mombasa"},
        "answer": "C"
    },
    {
        "question": "How many counties are in Kenya?",
        "choices": {"A": "47", "B": "39", "C": "49", "D": "41"},
        "answer": "A"
    },
    {
        "question": "Who is the goat in football?",
        "choices": {"A": "Neymar", "B": "Messi", "C": "Ronaldo", "D": "Maradona"},
        "answer": "B"
    },
    {
        "question": "Who won the last world cup tournament?",
        "choices": {"A": "Portugal", "B": "Brazil", "C": "Argentina", "D": "Spain"},
        "answer": "D"
    },
    {
        "question": "Who is the current president of Kenya?",
        "choices": {"A": "William Ruto", "B": "Uhuru Kenyatta", "C": "Moi", "D": "Kibaki"},
        "answer": "A"
    },
    {
        "question": "What is the square root of 9?",
        "choices": {"A": "5", "B": "3", "C": "2", "D": "6"},
        "answer": "B"
    }
]

random.shuffle(questions)
score = 0
total = len(questions)

print("=" * 40)
print("   WELCOME TO THE PYTHON QUIZ!")
print("=" * 40)

for i in range(total):
    q = questions[i]  
    print(f"\nQuestion {i+1}/{total}: {q['question']}")
    
    for key, choice in q["choices"].items():
        print(f"  {key}. {choice}")
    
    
    user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
    
    if user_answer in ["A", "B", "C", "D"]:
        if user_answer == q["answer"]:
            print("Correct! +1 point")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    else:
        print("Invalid input! No points for this question.")

print("\n" + "=" * 40)
print(f"      QUIZ COMPLETE!")
print(f"      Your Score: {score}/{total}")
print("=" * 40)