from flask import Flask, request, render_template_string

app = Flask(__name__)  # ✅ Biến này tên phải là 'app'

HTML = '''
<h1>Máy tính tuổi thông minh</h1>
<form method="post">
    <input type="number" name="age" required placeholder="Nhập tuổi">
    <input type="submit" value="Tính tuổi">
</form>
{% if age %}
<p>Bạn {{ age }} tuổi</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    if request.method == 'POST':
        age = request.form['age']
    return render_template_string(HTML, age=age)

# ❌ KHÔNG cần app.run() khi dùng Render
