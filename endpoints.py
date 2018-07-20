"""api module for user and diary entries"""
from flask import Flask
from flask import abort
from flask import jsonify
from flask import make_response
from mydatadb import DIARY_DB as diary_db
from mydatadb import DT as cdate
from flask import request

APP = Flask(__name__)

@APP.errorhandler(404)
def resource_not_found(error):
    """ this will handle 404 error: return json """
    return make_response(
        jsonify({'error': 'resource not found!!!!'}), 404)
        
@APP.route('/mydiary/v1/diaryentries', methods=['GET'])
def get_all_diary_entries():
    """Tis method will return all diary data stored"""
    return jsonify({'diary_db': diary_db})

@APP.route('/mydiary/v1/diaryentries/<int:entry_id>', methods=['GET'])
def get_one_diary_entry(entry_id):
    """this method will return one diary entry"""
    diary_entry = [diary_entry for diary_entry in diary_db if diary_entry['id'] == entry_id]
    if not diary_entry:
        return jsonify({'error':'expect title to be string'}),404
    return jsonify({'diary_entry': diary_entry[0]})

@APP.route('/mydiary/v1/diaryentries', methods=['POST'])
def new_diary_entry():
    """ add new diary entry to """
    if not request.json:
        abort(400)
    if not isinstance(request.json['title'],str):
        return jsonify({'error':'expect title to be string'}),400
    if not isinstance(request.json['data'],str):
        return jsonify({'error':'expect data to be string'}),400
    diary_entry = {
        'id': diary_db[-1]['id'] + 1,
        'date': cdate,
        'title': request.json['title'],
        'data': request.json['data']
    }
    diary_db.append(diary_entry)
    return jsonify({'new diary entry': diary_entry}), 201

if __name__ == '__main__':
    APP.run(debug=True)