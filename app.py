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
            height: 100%;
            background-color: #f0f2f5;
        }
        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            padding: 20px;
        }
        .container {
            text-align: center;
            padding: 40px 30px;
            border-radius: 15px;
            background-color: white;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 500px;
        }
        h1 {
            font-size: 8vw;
            margin-bottom: 30px;
            color: #007bff;
        }
        input[type="number"] {
            padding: 15px;
            font-size: 6vw;
            width: 80%;
            max-width: 300px;
            margin-bottom: 20px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        input[type="submit"] {
            padding: 15px 30px;
            font-size: 6vw;
            max-width: 100%;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        p {
            margin-top: 20px;
            font-size: 6vw;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="container">
            <h1>Máy tính tuổi</h1>
            <form method="post">
                <input type="number" name="age" placeholder="Nhập tuổi" required><br>
                <input type="submit" value="Tính">
            </form>
            {% if age %}
                <p>Bạn {{ age }} tuổi</p>
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

