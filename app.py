from flask import Flask, render_template

app = Flask (__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/Control")
def Control():
    return render_template('Control.html')


@app.route("/OOP")
def OOP():
    return render_template('OOP.html')


@app.route("/Pro")
def Pro():
    return render_template('Pro.html')



if __name__ == '__main__':
    app.run(debug=True)
