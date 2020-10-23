from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/liste')
def read_infra():
    with open("/home/osboxes/Documents/tp_flask/bdd.json", "r") as f:
        retour = json.load(f)
        return jsonify(retour) 

@app.route('/ajout', methods=['POST'])
def write_infra():
    try:
        data = json.loads(request.data)
        assert isinstance(data, dict)
    except:
        return "Invalid data", 400
    with open("/home/osboxes/Documents/tp_flask/bdd.json", "r") as f:
        tout = json.load(f)
        tout.append(data)
    
        with open("/home/osboxes/Documents/tp_flask/bdd.json", "w") as f:
            f.write(json.dumps(tout, sort_keys=True, indent=4))
            return jsonify(data)

@app.route('/liste/<nom>')
def machine(nom):
    with open("/home/osboxes/Documents/tp_flask/bdd.json", "r") as f:
        retour = json.load(f)
        for i in retour:
            if i["name"] == nom:
                return jsonify(i)
        return "cette machine n'existe pas", 404

@app.route('/liste/<nom>', methods=['DELETE'])
def delete(nom):
    with open("/home/osboxes/Documents/tp_flask/bdd.json", "r") as f:
        l = json.load(f)
        machine = {}
        for i in l:
            if i["name"] == nom:
                l.remove(i)
                machine = i
    with open("/home/osboxes/Documents/tp_flask/bdd.json", "w") as f:
        f.write(json.dumps(l, sort_keys=True, indent=4))
        return jsonify(machine)

