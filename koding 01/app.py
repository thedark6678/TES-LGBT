from flask import Flask, render_template, request

app = Flask(_name_)

def process_name(name):
    # Konversi nama jadi list karakter
    name = name.lower()
    new_name = ""
    for c in name:
        if c == 'a':
            new_name += '' if (12 >= 100) else c  # contoh pengurangan 12%
        elif c == 't':
            new_name += '' if (10 >= 100) else c  # contoh pengurangan 10%
        else:
            new_name += c
    return new_names

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        result = process_name(name)
    return render_template("index.html", result=result)

if _name_ == "_main_":
    app.run(debug=True)