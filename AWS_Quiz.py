class AWS_Quiz:
    def __init__(self):
        self.questions = [
            {"question": "Which of the following services provides managed relational databases in AWS?",
                "options": ["A. Amazon S3", "B. Amazon RDS", "C. Amazon EC2", "D. Amazon Redshift"],
                "answer": "B"},
            {"question": "Which of the following services provides serverless computing in AWS?",
             "options": ["A. Amazon EC2", "B. Amazon RDS", "C. AWS Lambda", "D. Amazon Route 53"],
             "answer": "C"},
            {"question": "Which of the following services provides object storage in AWS?",
             "options": ["A. Amazon RDS", "B. Amazon S3", "C. Amazon Redshift", "D. Amazon EC2"],
             "answer": "B"},
            {"question": "Which statement best describes Amazon DynamoDB?",
             "options": ["A. A service that enables you to run relational databases in the AWS Cloud",
                         "B. A serverless key-value database service",
                         "C. A service that you can use to migrate relational databases non relational databases "
                         "and other types of data stores",
                         "D. An enterprise-class relational database"],
             "answer": "B"},
            {"question": "Which of the following services provides a managed data warehouse service?",
             "options": ["A. Amazon S3", "B. Amazon EC2", "C. Amazon RDS", "D. Amazon Redshift"],
             "answer": "D"},
            {"question": "Which action can you perform with AWS Outposts?",
             "options": ["A. Automate actions for AWS services and applications through scripts",
                         "B. Access wizards and automated workflows to perform tasks in AWS services.",
                         "C. Develop AWS applications in supported programming languages.",
                         "D. Extend AWS infrastructure and services to your on-premises data center."],
             "answer": "D"},
            {"question": "Which of the following services provides a managed Elasticsearch service?",
             "options": ["A. Amazon RDS", "B. Amazon Elasticsearch Service", "C. Amazon Redshift",
                         "D. Amazon DynamoDB"],
             "answer": "B"},
            {"question": "Which of the following services provides a managed message queue service?",
             "options": ["A. Amazon SNS", "B. Amazon SQS", "C. Amazon S3", "D. Amazon Route 53"],
             "answer": "B"},
            {"question": "Which service helps protect your applications against distributed denial-of-service (DDoS) attacks?",
             "options": ["A. Amazon GuardDuty", "B. Amazon Inspector", "C. AWS Artifact", "D. AWS Shield"],
             "answer": "D"}
        ]
        self.score = 0

    def ask_question(self, question):
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ")
        if answer.lower() == question["answer"].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")

    def run_quiz(self):
        for question in self.questions:
            self.ask_question(question)
            print(f"You scored {self.score}/{len(self.questions)} points!")


quiz = AWS_Quiz()
quiz.run_quiz()
