# Diary_EndPoint

Rest Endpoints for my diary app
FEATURES:
    GET endpoint: fetch all /mydiary/v1/diaryentries
    GET endpoint: fetch one  /mydiary/v1/diaryentries/<int:id> 
    POST endpoint: create new /mydiary/v1/diaryentries
    PUT endpoint: modify one /mydiary/v1/diaryentries/<int:>
    DELETE endpoint: delete one /mydiary/v1/diaryentries/<int:>
    
REQUIREMENTS:
    install requirements.txt
    
HOW TO TEST ENDPOINTS:
    run endpoints.py and test endpoints with postman
       n.b accept json data only
           post {"title":"math contest","data":"it was a tough day.........."}
    run test_endpoints.py with pytest

  
