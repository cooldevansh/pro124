from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'contact':'9987644456',
        'Name': 'Raju',
        'Done': False,
        'id': 1

    },
    {
        'id':2,
        'Name': 'Rahul',
        'Done': False,
        'Contact': 9090992224

    },
]
@app.route('/')
def hello_world():
    return "hello who ever you are"
@app.route('/get-data')
def get_task():
    return jsonify({"data": tasks})
if(__name__=="__main__"):
    app.run(debug=True)