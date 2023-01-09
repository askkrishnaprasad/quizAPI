from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler API")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.label_score = Label(text="Score:", bg=THEME_COLOR)
        self.label_score.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Question Here", fill="black", font=("Arial", 20, "bold"))
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        photo_yes = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=photo_yes, highlightthickness=0, command=self.answer_true)
        self.yes_button.grid(column=1, row=3)

        photo_no = PhotoImage(file="images/false.png")
        self.no_button = Button(image=photo_no, highlightthickness=0, command=self.answer_false)
        self.no_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the Quiz.!")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

