from flask import Flask, request, send_from_directory, jsonify

question = []
app = Flask(__name__)
@app.route('/')
def index():
    return send_from_directory('static','index.html')

@app.route('/list')
def list():
    return send_from_directory('static','list.html')

@app.route('/submit',methods=['POST'])
def hello():
    new_question = {'name':request.form['name'],'email':request.form['email'],'subject':request.form['subject'],'message':request.form['message']}
    question.append(new_question)
    return send_from_directory('static','list.html')

@app.route('/get_questions')
def list_question():
    return jsonify(question)
if __name__ == '__main__':
    app.run()
