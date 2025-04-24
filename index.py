from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("0.html")        

if __name__ == "__main__":
    app.run()
