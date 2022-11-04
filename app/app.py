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
        # テキストボックスchickeet_contentに書かれた内容をchickeetに代入
        chickeet = request.form["chickeet_content"]
        # 実際に表示する6つの肯定意見を要素とするリストpositivelistを作成
        positivelist = []
        # 肯定意見のストックすべてを要素とするリストall_positivelistを作成
        all_positivelist = []
        # データベースをリスト形式にしたリストall_positive_queriesを作成
        all_positive_queries = PositiveContent.query.all()
        # all_positive_queriesの各要素（SQLで言う各行）について、行IDなどを排除し、肯定意見の文字列だけを抜き取り、all_positivelistに要素として追加
        for positive_query in all_positive_queries:
            all_positivelist.append(positive_query.body)
        # all_positivelistの中から要素を6つ重複を許さず選んだリストall_positivelist_randomを作成
        all_positivelist_random = random.sample(all_positivelist, k=6)
        # all_positivelist_randomのすべての要素をpositivelistに要素として追加
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