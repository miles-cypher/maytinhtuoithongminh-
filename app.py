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
            padding: 40px;
            border-radius: 12px;
            background-color: white;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            border: 1px solid #ddd;
        }
        h1 {
            font-size: 36px;
            color: #007bff;
            margin-bottom: 20px;
        }
        input[type="number"] {
            padding: 10px;
            font-size: 18px;
            width: 120px;
            margin-right: 10px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
        }
        p {
            margin-top: 20px;
            font-size: 20px;
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
