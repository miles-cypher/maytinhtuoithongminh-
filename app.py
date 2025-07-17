from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Máy tính tuổi thông minh</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            height: 100%;
        }
        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            text-align: center;
            padding: 40px 30px;
            border-radius: 15px;
            background-color: white;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 800px;
            min-width: 300px;
            margin: 0 auto;
        }
        h1 {
            font-size: clamp(28px, 5vw, 48px);
            color: #007bff;
            margin-bottom: 30px;
        }
        input[type="number"] {
            padding: 15px;
            font-size: clamp(18px, 4vw, 28px);
            width: 80%;
            max-width: 300px;
            margin-bottom: 20px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        input[type="submit"] {
            padding: 15px 30px;
            font-size: clamp(18px, 4vw, 28px);
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        p {
            margin-top: 20px;
            font-size: clamp(20px, 4vw, 32px);
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="container">
            <h1>Máy tính tuổi thông minh</h1>
            <form method="post">
                <input type="number" name="age" placeholder="Hãy nhập số tuổi" required><br>
                <input type="submit" value="Tính">
            </form>
            {% if age %}
                <p>Bạn {{ age }} tuổi rùi </p>
            {% endif %}
        </div>
    </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        age = request.form["age"]
    return render_template_string(HTML, age=age)
