from model import connect_to_db, db, Data
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def homepage():
    #shows homepage
    return 'index'

@app.route('/set', methods=['POST'])
def set_info():

    if request.is_json:
        data = request.get_json()

        datatable = Data.query.filter_by(key="key").first()
        if not datatable:
            datatable = Data(key="key", value="value")
            db.session.add(datatable)
            db.session.commit()
            response_body = {
                'message': 'JSON received, new key and value added to db',
                'key': data.get("key"),
                'value': data.get("value")
            }
        else:
            existing_key = Data.query.get("key")
            data.value = existing_key.value
            db.session.commit()
            response_body = {
                'message': 'JSON received, value has been updated',
                'key': data.get("key"),
                'value': data.get("value")
            }

        res = make_response(jsonify(response_body), 200)
        return res
    
    else:
        res = make_response(jsonify({'message': 'JSON not received'}), 400)
        return res

@app.route('/get', methods=['GET'])
def get_info():

    datatable = Data.query.filter_by("key")
    json_data = request.json
    json_key = json_data["key"]
    json_value = json_data["value"]

    return 

if __name__ == '__main__':
    #run app in debug mode on port 4000
    app.run(debug=True, port=4000)
    connect_to_db(app)