from model import connect_to_db, db, Data
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def homepage():
    #shows homepage
    return 'hello'

@app.errorhandler(Exception)
def handle_error(e):
    #returns user error and status code for 4XX errors
    if str(e) >= '400':
        return make_response(jsonify({
            'message': 'JSON not received, user error',
            'status code': str(e)}))
    #returns server error and status code for 5XX errors
    elif str(e) >= '500':
        return make_response(jsonify({
            'message': 'JSON not received, server error',
            'status code': str(e)}))
    #shows status code for all other errors
    raise e

@app.route('/set', methods=['POST'])
def set_info():
    #get key & value from json, check to see if it exists in db
    #if not add it to db, if it is replace with new value
    data = request.get_json()
    incoming_key = data['key']
    incoming_value = data['value']

    data_table = Data.query.filter_by(key=incoming_key).first()
    
    if not data_table:
        data_table = Data(key=incoming_key, value=incoming_value)
        db.session.add(data_table)
        db.session.commit()

        response_body = {
            'message': 'JSON received, new key and value added to db',
            'key': data.get("key"),
            'value': data.get("value"),
            'status code': '200'
        }

    else:
        Data.query.filter_by(key=incoming_key).update(dict(value=incoming_value))
        db.session.commit()
        response_body = {
            'message': 'JSON received, value has been updated',
            'key': data.get("key"),
            'new value': data.get("value"),
            'status code': '200'
        }
    
    res = make_response(jsonify(response_body), 200)
    return res

@app.route('/get', methods=['GET'])
def get_key():
    #get the key value that's included in /get?key=someKey url
    #if a parameter isn't passed, ask user to include key
    #if there is a parameter, query for the key in the db
    #if can't find, return message saying it's not in db
    search_key = request.args.get('key')

    if not search_key:
        response_body = {
            'message': "ERROR: key not input, please include the key you're searching for in the url parameters",
        }
    else:
        found_object = Data.query.filter_by(key=search_key).first()
        print(found_object)
        if found_object:
            found_key = found_object.key
            found_value = found_object.value
            print(found_value)
            response_body = {
                'key': found_key,
                'value': found_value,
            }
        else:
            response_body = {
                'message': 'ERROR: key not found in database',
            }
    res = make_response(jsonify(response_body), 200)
    return res

@app.route('/delete', methods=['POST'])
def delete_key():
    #get key from JSON, 
    #if no key input return message asking for key
    #if there is a key, query for the key in the db and delete
    #if key isn't in db, return message saying its not in db

    #could also make an error handler for 400 error in this specific endpoint
    incoming_data = request.get_json(silent=True)
    print(incoming_data)

    if incoming_data is None:
        response_body = {
            'message': "ERROR: key parameter is missing, please include the key you'd like to delete in the JSON POST body"
        }

    else:
        requested_key = incoming_data['key']
        found_key = Data.query.filter_by(key=requested_key).first()
        if found_key:
            found_key.delete()
            db.session.commit()
            response_body = {
                'message': "the key: " + found_key.key + " has been deleted"
            }
        else:
            response_body = {
                'message': "ERROR: key does not exist within database, please input existing key"
            }
    
    res = make_response(jsonify(response_body), 200)
    return res


if __name__ == '__main__':
    #run app in debug mode on port 4000
    connect_to_db(app)
    app.run(debug=True, port=4000)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['TRAP_HTTP_EXCEPTIONS'] = True