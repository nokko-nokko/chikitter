import random
from flask import Flask, render_template, request

#移動
app = Flask(__name__)

#追加
from app.models import db
from app.models import PositiveContent
import MeCab

# app = Flask(__name__)

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
        
        newpositivelist = []
        noun = ""
        for positive in positivelist:
            mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/ipadic -Ochasen")
            nouns = [line.split()[0] for line in mecab.parse(chickeet).splitlines() if "固有名詞" in line.split()[-1]]
            if len(nouns) == 0:
                newpositivelist = ["こんなにすごいと銅像建っちゃうよ","さすが👏","わかりみが深い","めちゃくちゃわかる","それなすぎて草","たしかに🦀"]
            else:
                noun = random.choice(nouns)
                newpositivelist.append(positive.replace('○○',noun))
        
        # 以下、アカウント名のランダム表示処理
        all_namelist = ['丹羽トリオ', 'チキンマン', 'しゃも山', '卵産みました!（7/31）','一ヶ月であなたも鷹になれる','チキ田']
        namelist = []
        all_namelist_random = random.sample(all_namelist, 6)

        for i in range(6):
            namelist.append(all_namelist_random[i])
        return render_template('result.html',chickeet=chickeet,positivelist=newpositivelist,namelist=namelist)
    
    #おまじない
if __name__ == "__main__":
    app.run(debug=True)