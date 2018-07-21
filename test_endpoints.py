"""testing module for endpoints"""
import pytest
import endpoints
from endpoints import APP as app

def test_diary_data():
    """data type should be of type list ...list of dictionaries"""
    assert isinstance(endpoints.diary_db, list)

def test_diary_urls():
    """testing my url path """
    with app.test_request_context('/mydiary/v1/diaryentries'):
        resp = endpoints.get_all_diary_entries()
        assert endpoints.request.path == '/mydiary/v1/diaryentries'

def test_get_all_diary_entries_status_code():
    """status code for get all should be ok: 200 """
    with app.test_request_context():
        resp = endpoints.get_all_diary_entries()
        assert resp.status_code, 200

def test_get_one_diary_entry_status_code():
    """status code for get one should be ok: 200 where id passed is valid """
    with app.test_request_context():
        resp = endpoints.get_one_diary_entry(2)
        assert resp.status_code, 200
