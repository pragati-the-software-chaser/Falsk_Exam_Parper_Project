import json
import os
from flask import Flask ,request, jsonify

app = Flask(__name__)
@app.route('/addSubject',methods=["POST"])
def add_subject():
    input_json = request.get_json(force=True) 
    print(input_json)
    subject_name=input_json["subject_name"]
    file = open ("examfile.json", "r")
    content = file.read()
    content=json.loads(content)
    subject=content["Subject"]
    subject[subject_name] ={ }
    file = open ("examfile.json", "w")
    content=json.dumps(content,indent=4)
    file.write(content)
    file.close()
    return "Success add_subject"
@app.route('/add_question',methods=["POST"])
def add_question (): 
    input_json = request.get_json(force=True) 
    subject_name=input_json["subject_name"]
    question_number=input_json["question_number"]
    question_discription=input_json["question_discription"]
    # Read a json file (Syntax= file = open ("file_name/Path", "r"), where file -> object , content -> variable)
    file = open ("examfile.json", "r")
    content = file.read()
    # json string to python dictionary (json.loads(file/variable)) 
    content=json.loads(content)
    # Reading "Subject from the json file as a key in content dict , and assigning to the subject variable"
    subject = content["Subject"]
    # subject[key]={value :"String"}
    subject_question=subject[subject_name]
    subject_question[question_number] =question_discription
    #print the content
    print(content)
    # write the content in to json file (open,write,close), (need to dumps from python o json Syntax : json.dumps(file))
    file = open ("examfile.json", "w")
    # indent = number to beutify the json file
    content=json.dumps(content,indent=4)
    file.write(content)
    file.close()
    return "Success add_question"
@app.route('/update_question',methods=["POST"])
def update_question():
    input_json = request.get_json(force=True) 
    subject_name=input_json["subject_name"]
    question_number=input_json["question_number"]
    updated_question_discription=input_json["updated_question_discription"]
    file = open("examfile.json", "r")
    content = file.read()
    content=json.loads(content)
    print(content)
    subject=content["Subject"]
    subject_question=subject[subject_name]
    subject_question[question_number] =updated_question_discription
    file = open ("examfile.json", "w")
    content=json.dumps(content,indent=4)
    file.write(content)
    file.close()
    return "Success update_question"
@app.route('/delete_question',methods=["POST"])  
def delete_question():
    input_json = request.get_json(force=True) 
    subject_name=input_json["subject_name"]
    question_number=input_json["question_number"]
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
    return "Success delete_question"
@app.route('/delete_subject',methods=["POST"])       
def delete_subject():
    # for "Post"
    input_json = request.get_json(force=True) 
    subject_name = input_json["subject_name"]
    file = open("examfile.json", "r")
    content = file.read()
    content=json.loads(content)
    subject_pop=content["Subject"]
    subject_pop.pop(subject_name)
    file = open ("examfile.json", "w")
    content=json.dumps(content,indent=4)
    file.write(content)
    file.close()
    return "Success delete_subject"

@app.route('/getSubjects',methods=["GET"])       
def get_subjects():
   
    file = open("examfile.json", "r")
    content = file.read()
    content=json.loads(content)
    get_subject=content["Subject"]
    Ans_get_subject=get_subject.keys()
    list_subject=tuple(Ans_get_subject)
    result ={"subjectnames" : list_subject}
    file.close()
    return result

@app.route('/getSubjectQuestions',methods=["GET"])       
def get_subjects_questions():
    subject_name = request.args.get("subject_name")
    file = open("examfile.json", "r")
    content = file.read()
    content=json.loads(content)
    get_subject=content["Subject"]
    Ans_get_subject_queston=get_subject[subject_name]
    file.close()
    return Ans_get_subject_queston