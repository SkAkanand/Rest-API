from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for audio elements
audio_elements = []

# Helper function to find audio element by ID
def find_audio_element(audio_id):
    for audio in audio_elements:
        if audio['id'] == audio_id:
            return audio
    return None

# API endpoint to get all audio elements
@app.route('/audio-elements', methods=['GET'])
def get_audio_elements():
    return jsonify(audio_elements)

# API endpoint to get a specific audio element by ID
@app.route('/audio-elements/<int:audio_id>', methods=['GET'])
def get_audio_element(audio_id):
    audio = find_audio_element(audio_id)
    if audio:
        return jsonify(audio)
    return jsonify({'error': 'Audio element not found'}), 404

# API endpoint to create a new audio element
@app.route('/audio-elements', methods=['POST'])
def create_audio_element():
    data = request.get_json()
    audio_id = len(audio_elements) + 1
    audio = {'id': audio_id, 'name': data['name'], 'duration': data['duration']}
    audio_elements.append(audio)
    return jsonify(audio), 201

# API endpoint to update an existing audio element
@app.route('/audio-elements/<int:audio_id>', methods=['PUT'])
def update_audio_element(audio_id):
    audio = find_audio_element(audio_id)
    if audio:
        data = request.get_json()
        audio['name'] = data['name']
        audio['duration'] = data['duration']
        return jsonify(audio)
    return jsonify({'error': 'Audio element not found'}), 404

# API endpoint to delete an audio element
@app.route('/audio-elements/<int:audio_id>', methods=['DELETE'])
def delete_audio_element(audio_id):
    audio = find_audio_element(audio_id)
    if audio:
        audio_elements.remove(audio)
        return jsonify({'message': 'Audio element deleted'})
    return jsonify({'error': 'Audio element not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
