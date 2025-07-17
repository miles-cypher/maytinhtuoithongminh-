from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<h2>Máy tính tuổi thông minh</h2>
<form method="post">
    Nhập tuổi: <input type="number" name="age" required>
    <input type="submit" value="Gửi">
</form>
{% if age %}
<p>Bạn {{ age }} tuổi</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        age = request.form["age"]
    return render_template_string(HTML, age=age)

if __name__ == "__main__":
    app.run()
