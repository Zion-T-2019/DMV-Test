from lxml import etree


class XmlParser:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.questions = []
    
    def parse_questions(self):
        #parse the xml file and return a list of questions
        self.xml_file = etree.parse(self.xml_file)
        self.root = self.xml_file.getroot()
        for question_elem in self.root.findall('question'):
            question = {
                'questionText': question_elem.find('questionText').text,
                'questionImage': question_elem.find('questionImage').get('path') if question_elem.find('questionImage') is not None else None,
                'answers': [],
                'answerComments': question_elem.find('answerComments').text
            }

            for answer_elem in question_elem.findall('answer'):
                answer = { 
                    'text': answer_elem.text,
                    'correct': answer_elem.get('correct', 'false') == 'true'
                }
                question['answers'].append(answer)

            self.questions.append(question)

        return self.questions
