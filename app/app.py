import random
from flask import Flask, render_template, request
from models.models import PositiveContent

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/howto')
def howto():
    return render_template('howto.html')
    
@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == "POST":
        chickeet = request.form["chickeet_content"]
        positivelist = []
        all_positivelist = []
        all_positive_queries = PositiveContent.query.all()
        for positive_query in all_positive_queries:
            all_positivelist.append(positive_query.body)
        all_positivelist_random = random.sample(all_positivelist, k=6)
        for i in range(6):
            positivelist.append(all_positivelist_random[i])
        return render_template('result.html',chickeet=chickeet,positivelist=positivelist)
    else:
        chickeet = "おにぎりは鮭しか勝たん"
        positivelist = ["やるやん","僕もそう思います","おにぎり最高！","時代は鮭","まじで同感","おいしいよね"]
        return render_template('result.html',chickeet=chickeet,positivelist=positivelist)

    #おまじない
if __name__ == "__main__":
    app.run(debug=True)