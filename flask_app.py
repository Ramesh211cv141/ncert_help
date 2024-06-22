from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI with your API key
openai.api_key = 'sk-proj-9H9nTXBQRd34IgObRulRT3BlbkFJTAwANLjer4grqfv6fgr0'
assistant_id = 'asst_d0EL2uqJr4G7t3ig2fLRrOxl' 

def get_openai_response(prompt, assistant_id):
    messages = [
        {"role": "system", "content": f"{assistant_id}"},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content'].strip()

@app.route('/questions', methods=['GET'])
def get_questions():
    topic = request.args.get('topic')
    num_questions = request.args.get('num', default=1, type=int)
    prompt = f"Generate {num_questions} questions on the topic: {topic}"
    questions = get_openai_response(prompt, assistant_id)
    return jsonify({"questions": questions})

@app.route('/rephrase', methods=['POST'])
def rephrase_question():
    data = request.json
    question = data.get('question')
    prompt = f"Rephrase the following question:\n\n{question}\n\nProvide the rephrased question."
    rephrased_question = get_openai_response(prompt, assistant_id)
    return jsonify({"rephrased_question": rephrased_question})

if __name__ == '__main__':
    app.run(debug=True)


