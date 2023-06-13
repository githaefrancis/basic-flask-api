from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route("/<name>")
def Home(name):
    extras=request.args.get('extras')
    return f"Home {name} {extras}"
    
@app.route("/create-user",methods=["POST"])
def Create():
    user= request.get_json()
    print(user)
    user['id']=22
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)