'''
7. Simple Quiz System
Context: A training platform needs to administer quizzes.

Task: Create two classes:

Question with attributes: text, options (list of strings), correct_answer (index).

Quiz with attributes: questions (list of Question), score (int).

Methods:

add_question(question).

take_quiz() – loops through each question, prints text and options, takes user input (simulate with a provided answer list), checks correctness, updates score.

get_score() – returns score.

Static method: load_from_dict(data) – creates a Quiz from a dictionary structure (optional).

Sample Usage:

q1 = Question("What is 2+2?", ["3", "4", "5"], 1)
q2 = Question("What is the capital of France?", ["London", "Paris", "Berlin"], 1)
quiz = Quiz()
quiz.add_question(q1)
quiz.add_question(q2)
quiz.take_quiz(answers=[1, 1])  # simulate answers  -> a bteter way is ask input directly one by one
print(quiz.get_score())  # 2
'''

class Question:
    def __init__(self,text,option,ans):
        self.text = text
        self.option = option
        self.ans = ans

class Quiz:
    
    def from_dict(data):
        text = data['text']
        op = data['option']
        ans = data['ans']
        q = Question(text,op,ans)
        quiz = Quiz()
        quiz.add_question(q)
        return quiz

    def __init__(self):
        self.questions = []
        self.score = 0
    def add_question(self,q):
        self.questions.append(q)
        return "Question added"
    
    def take_quiz(self):
        for i in self.questions:
            print(f"{i.text} \t {i.option}")
            user = int(input("Enter correct answer index: "))
            if user == i.ans:
                print("Correct answer")
                self.score+=1
            else:
                print("Incorrect answer")

    def get_score(self):
        return self.score
    
        
quiz_data = {
    "text": "What is 2+2?",
    "option": ["3", "4", "5"],
    "ans": 1
}

quiz = Quiz.from_dict(quiz_data)
quiz.take_quiz()
quiz.get_score()


q1 = Question("What is 2+2?", ["3", "4", "5"], 1)
q2 = Question("What is the capital of France?", ["London", "Paris", "Berlin"], 1)
quiz = Quiz()
quiz.add_question(q1)
quiz.add_question(q2)
quiz.take_quiz()  # simulate answers
print(quiz.get_score())  # 2

