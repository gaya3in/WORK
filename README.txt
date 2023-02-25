API EndPoints:
   
localhost:8000/api/register:
  User Registeration API
localhost:8000/api/works/:
  API to list down all the work data in the work table
  Fields displayed in the api : id, link, type, artist
localhost:8000/api/works?type=Other:
   API to filter data based on work type.
   Fields displayed in the api : id, link, type, artist
http://localhost:8000/api/works/?search=Name3:
   API to serach data based on artist name
   Fields displayed in the api : id, link, type, artist