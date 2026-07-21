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


# q1 = Question("What is 2+2?", ["3", "4", "5"], 1)
# q2 = Question("What is the capital of France?", ["London", "Paris", "Berlin"], 1)
# quiz = Quiz()
# quiz.add_question(q1)
# quiz.add_question(q2)
# quiz.take_quiz()  # simulate answers
# print(quiz.get_score())  # 2

