
from flask import Flask, jsonify, request
from flask_cors import CORS

import my_repository

app = Flask(__name__)
CORS(app)

my_mongo_agent = my_repository.MyMongoAgent()

@app.route('/')
def hello_world():
   return 'Welcome Everyone! :)'

@app.route('/dogs')
def get_all_dogs():
    try:
        return jsonify(my_mongo_agent.get_all_dogs()), 200
    except Exception as e:
        return jsonify({"message":"Error occurred" ,"err":str(e)}), 500

@app.route('/dogs/<id>', methods=['GET'])
def get_dog_by_id(id):
    try:
        response = my_mongo_agent.get_dog_by_id(id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"message":"Error occurred" ,"err":str(e)}), 500

@app.route('/dogs',methods=["POST"])
def insert_new_dog():
    # TODO: add input validations - on bad input return error with code 400
    try:
        # get the data from the request body
        # and send to our 'repository'
        response = my_mongo_agent.insert_dog(request.json)

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"message":"Error occurred" ,"err":str(e)}), 500

@app.route('/dogs/<id>', methods=['DELETE'])
def delete_dog(id):
    try:
        response = my_mongo_agent.delete_dog_by_id(id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"message":"Error occurred" ,"err":str(e)}), 500

@app.route('/dogs/<id>', methods=['PUT'])
def update_record(id):
    # TODO: add input validations - on bad input return error with code 400
    try:
        response = my_mongo_agent.update_dog_by_id(id, request.json)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"message":"Error occurred" ,"err":str(e)}), 500

def test_dogs_mongo_db():

    # my_mongo_agent.get_all_dogs()
    #
    #  my_mongo_agent.insert_dog({"name":"Rocky","birthYear":2000, "breed":"German Shepherd"})
    #   x = my_mongo_agent.get_all_dogs()
    #   print(x)
    #  my_mongo_agent.update_dog_by_id("676a8aff56d052010dc657f0",{"name":"Miric"})
    # my_mongo_agent.update_dog0()
    # my_mongo_agent.get_all_dogs()
    #
    # my_mongo_agent.update_dog()
    # my_mongo_agent.get_all_dogs()

    # my_mongo_agent.delete_dog_by_id("676a672f529f6fcb7b0c0465")
    x = my_mongo_agent.get_all_dogs()
    print(x)

    x = my_mongo_agent.get_dog_by_id("676a666c529f6fcb7b0c0464")
    print(x)

#test_dogs_mongo_db()

# ============================================
# === Make sure this line at the end of file
if __name__ == '__main__':
    print("hello from app.py")
    # run app in debug mode on port 5000
    # app.run(debug=True, port=5730)
    app.run( debug=True, port=5730)
# ============================================