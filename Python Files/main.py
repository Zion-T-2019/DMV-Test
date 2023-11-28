from xmlparser import XmlParser
import lxml

def main():
    
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