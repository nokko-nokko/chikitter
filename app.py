from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/howto')
def howto():
    return render_template('howto.html')
    
@app.route('/result')
def result():
    return render_template('result.html')


    #おまじない
if __name__ == "__main__":
    app.run(debug=True)