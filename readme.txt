#swagger :https://realpython.com/flask-connexion-rest-api/#the-people-rest-api
# if module is not found after package installation , check the virtual environment
#in stand alone system run app.py file via 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

#postman : run app.py ,flask run , copy the path 
in postman : path/route/requiredparameters
http://127.0.0.1:5000/getSubjectQuestions?subject_name=EC
# https://nordicapis.com/how-to-create-an-api-using-the-flask-framework/