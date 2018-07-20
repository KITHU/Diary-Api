"""api module for user and diary entries"""
from flask import Flask
from flask import abort
from flask import jsonify
from flask import make_response
from mydatadb import DIARY_DB as diary_db
from mydatadb import DT as cdate
from flask import request

APP = Flask(__name__)


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


if __name__ == '__main__':
    APP.run(debug=True)