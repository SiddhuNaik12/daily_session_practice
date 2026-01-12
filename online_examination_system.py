# Set 6 (Online Examination System)
# An exam portal evaluates different types of questions.
# Scenario:
# Abstract class Question with method evaluate()


# Subclasses: MCQQuestion, CodingQuestion


# Requirements:
# MCQ evaluated by matching answers


# Coding evaluated by test case pass percentage


# Compute total score using dynamic method dispatch
from abc import ABC,abstractmethod
class Question(ABC):
    def __init__(self,marks):
        self.marks=marks
    @abstractmethod
    def evaluate():
        pass
class MCQQuestion(Question):
    def __init__(self,marks,correct,given):
        super().__init__(marks)
        self.correct=correct
        self.given=given
    def evaluate(self):
        if self.correct==self.given:
            return self.marks
        else:
            return 0

class CodingQuestion(Question):
    def __init__(self,marks,pass_percentage):
        super().__init__(marks)
        self.pass_percentage=pass_percentage
    def evaluate(self):
        return(self.marks * self.pass_percentage)//100
questions=[MCQQuestion(20,"A","A"),MCQQuestion(20,"B","C"),CodingQuestion(20,75)]
total_score=0
for q in questions:
    total_score = total_score+q.evaluate()
print("total_score=",total_score)
