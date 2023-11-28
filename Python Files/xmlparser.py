from lxml import etree


class XmlParser:
    def __init__(self, xml_file):
        ## pass and parse xml file 
        pass
    
    def parse_questions(self):
        questions = []

        for question_elem in self.root.findall('question'):
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
