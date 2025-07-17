from flask import Flask, request, render_template_string

app = Flask(__name__)  # ✅ PHẢI là tên app

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Máy tính tuổi</title></head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh">
  <div>
    <h1>Máy tính tuổi thông minh</h1>
    <form method="post">
      <input type="number" name="age" placeholder="Nhập tuổi" required>
      <input type="submit" value="Tính">
    </form>
    {% if age %}
      <p>Bạn {{ age }} tuổi</p>
    {% endif %}
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

# ❌ KHÔNG cần app.run() trên Render
