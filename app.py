from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key="")

app = Flask(__name__)

  # Add your OpenAI API key here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan():
    country = request.form['country']
    vacation_type = request.form['vacation_type']

    # New ChatGPT API prompt
    prompt = f"Suggest a {vacation_type} vacation in {country}. Provide suggestions of things to do."

    # Use ChatCompletion (ChatGPT API) for the new interface
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a vacation planner."},
        {"role": "user", "content": prompt}
    ])
    vacation_plan = response.choices[0].message.content.strip()

    return render_template('plan.html', vacation_plan=vacation_plan)

if __name__ == '__main__':
    app.run(debug=True)
