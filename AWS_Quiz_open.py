import random

# Define a list of questions and their corresponding answers
questions = [
    {"question": "What does S3 stand for?", "answer": "Simple Storage Service"},
    {"question": "What is EC2?", "answer": "Elastic Compute Cloud"},
    {"question": "What is the name of AWS's managed database service?", "answer": "RDS"},
    {"question": "What is the name of AWS's serverless computing platform?", "answer": "Lambda"},
    {"question": "What is the name of AWS's content delivery network?", "answer": "CloudFront"},
    {"question": "What is the name of AWS's message queuing service?", "answer": "SQS"},
    {"question": "What is the name of AWS's container service?", "answer": "ECS"},
    {"question": "What is the name of AWS's Kubernetes service?", "answer": "EKS"}
]

# Shuffle the questions
random.shuffle(questions)

# Define a variable to keep track of the user's score
score = 0

# Loop through each question and ask the user to answer it
for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    answer = input("Your answer: ")
    if answer.lower() == q['answer'].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {q['answer']}")

# Print the user's final score
print(f"You scored {score}/{len(questions)}")
