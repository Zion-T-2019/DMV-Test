class Question:
    def __init__(self, question_text, answer, ui=None):
        self.question_text = question_text
        self.answer = answer
        self.ui = ui  

    def set_text(self, question_text):
        self.question_text = question_text
        if self.ui:
            self.ui.question_index.setText(self.question_text)

    def set_answer(self, answer_text):
        self.answer = answer_text

    def check_answer(self, answer_text):
        return self.answer == answer_text

    def display(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # If the question has an image, display it
        if hasattr(self, 'image') and self.ui:
            self.ui.question.setPixmap(QtGui.QPixmap(self.image))

        # Display the question text
        if self.ui:
            self.ui.question_index.setText(self.question_text)
