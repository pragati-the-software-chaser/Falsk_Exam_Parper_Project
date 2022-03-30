import json
import os
class exam:
    def add_subject(self,subject_name ):
        file = open ("examfile.json", "r")
        content = file.read()
        content=json.loads(content)
        subject=content["Subject"]
        content[subject_name] ={ }
        file = open ("examfile.json", "w")
        content=json.dumps(content,indent=4)
        file.write(content)
        file.close()
    def add_question (self,subject_name, question_number, question_discription): 
        # Read a json file (Syntax= file = open ("file_name/Path", "r"), where file -> object , content -> variable)
        file = open ("examfile.json", "r")
        content = file.read()
        # json string to python dictionary (json.loads(file/variable)) 
        content=json.loads(content)
        # Reading "Subject from the json file as a key in content dict , and assigning to the subject variable"
        subject = content["Subject"]
        # subject[key]={value :"String"}
        subject[subject_name] ={question_number:question_discription}
        #print the content
        print(content)
        # write the content in to json file (open,write,close), (need to dumps from python o json Syntax : json.dumps(file))
        file = open ("examfile.json", "w")
        # indent = number to beutify the json file
        content=json.dumps(content,indent=4)
        file.write(content)
        file.close()
    def update_question(self, subject_name, question_number, updated_question_discription ):
        file = open("examfile.json", "r")
        content = file.read()
        content=json.loads(content)
        print(content)
        subject=content["Subject"]
        subject[subject_name] = {question_number : updated_question_discription}
        file = open ("examfile.json", "w")
        content=json.dumps(content,indent=4)
        file.write(content)
        file.close()
    def delete_question(self,subject_name,question_number):
        file = open("examfile.json", "r")
        content = file.read()
        content=json.loads(content)
        print(content)
        subject=content["Subject"]
        question=subject[subject_name]
        question.pop(question_number)
        file = open ("examfile.json", "w")
        content=json.dumps(content,indent=4)
        file.write(content)
        file.close()
    def delete_subject(self, subject_name):
        file = open("examfile.json", "r")
        content = file.read()
        content=json.loads(content)
        content.pop(subject_name)
        file = open ("examfile.json", "w")
        content=json.dumps(content,indent=4)
        file.write(content)
        file.close()

if __name__== "__main__":
    e=exam()
    #e.add_question("Math","Q1.", "What is 2+2?")
    #e.update_question("Math","Q1.", "What is 2+2*2?")
    #e.delete_question("Math","Q1.")
    #e.add_subject("Math")
    #e.delete_subject("Math")