HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Máy tính tuổi thông minh</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
        }
        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .container {
            text-align: center;
            padding: 50px;
            border-radius: 15px;
            background-color: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.15);
            border: 1px solid #ccc;
        }
        h1 {
            font-size: 48px;
            color: #007bff;
            margin-bottom: 40px;
        }
        input[type="number"] {
            padding: 20px;
            font-size: 24px;
            width: 200px;
            margin-right: 10px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        input[type="submit"] {
            padding: 20px 40px;
            font-size: 24px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        p {
            margin-top: 30px;
            font-size: 30px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="container">
            <h1>Máy tính tuổi thông minh</h1>
            <form method="post">
                <input type="number" name="age" placeholder="Nhập tuổi" required>
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
