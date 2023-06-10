class QuizBrain:

    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
      
    def check_answer(self,user_ans,correct_ans):
        if(user_ans.lower() == correct_ans.lower()):
          print("Right answer")
          return True
        else :
          print("Wrong Answer") 
          return False

    def get_score(self,b) :
        if b :
          self.score+=1
        print(f"Your current score is : {self.score}/12")
          

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_ans =input(
            f"Q.{self.question_number+1}: {current_question.text} (True/Flase): "
        )
        self.question_number += 1
        self.get_score(self.check_answer(user_ans,current_question.answer))
                             


    
        
