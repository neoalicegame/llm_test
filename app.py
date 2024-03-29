from flask import Flask, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)
llm = Ollama(model="llama2")

@app.route('/ask', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        data = request.get_json()
        question = data['question']
        response = llm.invoke(question)
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
