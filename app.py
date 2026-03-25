from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# PREDICT API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    attendance = data["attendance"]
    sessional = data["sessional_marks"]
    midterm = data["midterm_marks"]
    assignments = data["assignments"]
    study = data["study_hours"]

    # 🎯 WEIGHTED SCORE
    score = (
        attendance * 0.2 +
        sessional * 0.2 +
        midterm * 0.25 +
        assignments * 0.15 +
        (study * 20) * 0.2
    )

    # 🎯 LEVEL
    if score >= 75:
        level = "Good"
    elif score >= 50:
        level = "Average"
    else:
        level = "At Risk"

    # 🎯 SMART SUGGESTIONS
    suggestions = []

    if attendance < 75:
        suggestions.append("Attend remaining classes regularly")

    if assignments < 60:
        suggestions.append("Complete assignments properly")

    if study < 3:
        suggestions.append("Increase daily study hours")

    if midterm < 50:
        suggestions.append("Revise weak topics for final exam")

    if sessional < 50:
        suggestions.append("Focus on final exam to improve score")

    if score < 50:
        suggestions.append("High risk: Prepare seriously for final exam")

    return jsonify({
        "performance_score": round(score, 2),
        "performance_level": level,
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(debug=True)