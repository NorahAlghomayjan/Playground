from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<x>')
@app.route('/play/<x>/<color>')
def play3(x=1,color="lightblue"):
    return render_template("index3.html",count=int(x),backgroundcolor=color)

# @app.route('/play')
# def play():
#     return render_template("index2.html")
# @app.route('/play/<x>')
# def play2(x):
#     return render_template("index.html",count=int(x))

# @app.route('/play/<x>/<color>')
# def play3(x,color):
#     return render_template("index3.html",count=int(x),backgroundcolor=color)


if __name__=="__main__":
    app.run(debug=True)

