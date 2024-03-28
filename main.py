from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    
    if not data or 'message' not in data:
        return jsonify({'error': 'Invalid request. Message not found.'}), 400
    
    message = data['message']
    
    stream = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': message}],
        stream=True
    )
    
    response = ''
    for chunk in stream:
        response += chunk['message']['content']
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
