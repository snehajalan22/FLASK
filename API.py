from flask import Flask 
app=Flask(__name__)
tasks=[
    {
        "id":1,
        "contact":"9831702146",
        "name":"Shabd",
        "done":False
    },
    {
        "id":2,
        "contact":"8130718796",
        "name":"Paras",
        "done":False
    }
]
@app.route("/")
def hello_world():
    return "hello world"

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data",
        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "contact":request.json["contact"],
        "name":request.json.get("name",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
            "status":"error",
            "message":"task added succesfully",
        },400)
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if __name__=="__main__":
    app.run(debug=True)