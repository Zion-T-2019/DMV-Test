from xmlparser import XmlParser
from PyQt5 import QtCore, QtGui, QtWidgets


class ChoiceQuestion:
    def __init__(self, answer_comments):
        self.choices = []
        self.answer_comments = answer_comments
            
    def add_choice(self, choice, correct):
        # choice (str): The text of the choice.
        # correct (bool): True if the choice is correct, False otherwise.
        self.choices.append((choice, correct))
    
    def set_answer_comments(self, answer_comments):
        # answer_comments (str): Comments to be displayed when the user checks the answer.
        self.answer_comments = answer_comments
    
    def display(self, layout): 
        # layout (QtLayout): The layout to which the question will be added.
        # Creating a group for radio buttons
        group_box = QtWidgets.QGroupBox("Choices")
        group_layout = QtWidgets.QVBoxLayout()

        # Adding radio buttons for each choice
        for choice_text, _ in self.choices:
            radio_button = QtWidgets.QRadioButton(choice_text)
            group_layout.addWidget(radio_button)

        group_box.setLayout(group_layout)

        # Adding group box and answer comments label to the main layout
        layout.addWidget(group_box)
        layout.addWidget(QtWidgets.QLabel(f"Answer Comments: {self.answer_comments}"))
