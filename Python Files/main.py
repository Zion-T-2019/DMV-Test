from xmlparser import XmlParser
import lxml
import sys
from dmvdrivertestUI import UiMainWin
from PyQt5.QtWidgets import *

def main():
    # Insert the path the xml
    xml_file = "florida_drivers_test.xml"
    parser = XmlParser(xml_file)
    questions = parser.parse_questions()

    # Initialize the application
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    ui =  UiMainWin(questions)
    
   
        
    # Set up the UI
    ui.setup_ui(main_win)
    main_win.show()
    sys.exit(app.exec_())


main()