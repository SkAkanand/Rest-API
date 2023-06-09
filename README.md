# Rest-API
 you can run the application by executing the main.py file. The API endpoints will be accessible at http://localhost:5000/
 
 To test the API, you can use tools like cURL
 **Get all audio elements (GET request):**
 curl -X GET http://localhost:5000/audio-elements

**Add a new audio element (POST request):**
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "name": "Audio 1"}' http://localhost:5000/audio-elements

**Get a specific audio element (GET request):**
curl -X GET http://localhost:5000/audio-elements/1

**Update an audio element (PUT request):**
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Audio 1"}' http://localhost:5000/audio-elements/1

**Delete an audio element (DELETE request):**
  `curl -X DELETE http://localhost:5000/audio-elements/1
