from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_questions():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, option_a, option_b, option_c, option_d, correct FROM questions")
    rows = cursor.fetchall()
    conn.close()
    questions = [
        {"id": row[0], "text": row[1], "options": [row[2], row[3], row[4], row[5]], "correct": row[6]}
        for row in rows
    ]
    return questions

best_score = 0

@app.route('/')
def quiz():
    global best_score
    questions = get_questions() 
    return render_template('quiz.html', questions=questions, best_score=best_score)

@app.route('/submit', methods=['POST'])
def submit():
    global best_score
    user_answers = request.form
    score = 0

    questions = get_questions()

    for question in questions:
        question_id = f"question{question['id']}"
        if question_id in user_answers and user_answers[question_id] == question['correct']:
            score += 1

    total_questions = len(questions)
    percentage_score = int((score / total_questions) * 100)

    if percentage_score > best_score:
        best_score = percentage_score

    return render_template('result.html', score=percentage_score, best_score=best_score)

if __name__ == '__main__':
    app.run(debug=True)