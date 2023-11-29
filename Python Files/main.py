from xmlparser import XmlParser
import lxml
import sys
from dmvdrivertestUI import UiMainWin
from PyQt5.QtWidgets import *

def main():
    
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    ui = UiMainWin()
    ui.setup_ui(main_win)
    main_win.show()
    sys.exit(app.exec_())
    
    # Insert the path the xml
    xml_file = "questions.xml"
    parser = XmlParser(xml_file)
    questions = parser.parse_questions()

    # Print parsed information
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        
        # Pass question image and text
        print(f"Text: {question['questionText']}")
        print(f"Image Path: {question['questionImage']}")
        
        print("Answers:")
        for j, answer in enumerate(question['answers'], 1):
            print(f"  {j}. {answer['text']} (Correct: {answer['correct']})")
            
        print(f"Comments: {question['answerComments']}")

main()