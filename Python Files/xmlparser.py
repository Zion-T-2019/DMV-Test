import lxml
from lxml.etree import ElementTree as ET


class XmlParser:
    def __init__(self, xml_file):
        # Instantiating elment tree and root to parse xml file
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def parse_questions(self, element):
        # Intiating a list for the questions
        questions = []


        for question_elem in element.findall('question'):
            question = {
                'questionText': question_elem.find('questionText').text,
                'questionImage': question_elem.find('questionImage').get('path'),
                'answers': [],
                'answerComments': question_elem.find('answerComments').text
            }

            for answer_elem in question_elem.findall('answer'):
                answer = {
                    'text': answer_elem.text,
                    'correct': answer_elem.get('correct', 'false') == 'true'
                }
                question['answers'].append(answer)

            questions.append(question)

        return questions
    
    # Parsing through all elements
    def parse(self):
        self.parse_questions(self.root)
