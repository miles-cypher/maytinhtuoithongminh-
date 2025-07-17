from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Máy tính tuổi thông minh</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }
        .container {
            text-align: center;
            border: 2px solid #007bff;
            padding: 40px;
            border-radius: 15px;
            background-color: #fff;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h1 {
            font-size: 36px;
            margin-bottom: 20px;
            color: #007bff;
        }
        input[type=number] {
            padding: 10px;
            font-size: 16px;
            width: 100px;
            margin-right: 10px;
        }
        input[type=submit] {
            padding: 10px 20px;
            font-size: 16px;
            bac
