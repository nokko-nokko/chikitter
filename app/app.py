import random
from flask import Flask, render_template, request
from models.models import PositiveContent
# import MeCab
# GiNZA・spaCyに変更
import spacy
nlp = spacy.load('ja_ginza')

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
        # 実際に表示する6つの肯定意見を要素とするリストpositivelist1（固有名詞なし）、2（あり）を作成
        positivelist1 = []
        positivelist2 = []
        # 肯定意見のストックすべてを要素とするリストall_positivelistを作成
        all_positivelist = []
        # データベースをリスト形式にしたリストall_positive_queriesを作成
        all_positive_queries = PositiveContent.query.all()
        # all_positive_queriesの各要素（SQLで言う各行）について、行IDなどを排除し、肯定意見の文字列だけを抜き取り、all_positivelistに要素として追加
        for positive_query in all_positive_queries:
            all_positivelist.append(positive_query.body)
        
        all_positivelist1 = [s for s in all_positivelist if '○○' not in s]
        all_positivelist2 = [s for s in all_positivelist if '○○' in s]

        all_positivelist_random1 = random.sample(all_positivelist1, k=6)
        all_positivelist_random2 = random.sample(all_positivelist2, k=6)
        for i in range(6):
            positivelist1.append(all_positivelist_random1[i])
            positivelist2.append(all_positivelist_random2[i])
        
        newpositivelist = []
        noun = ""
        
        # mecab = MeCab.Tagger("-Ochasen")
        # nouns = [line.split()[0] for line in mecab.parse(chickeet).splitlines() if "固有名詞" in line.split()[-1]]

        # GiNZA・spaCyに変更
        noun_toks = []
        nouns = []
        for tok in nlp(chickeet):
            if tok.pos_ in ('PROPN'):
                noun_toks.append(tok)
        for tok in noun_toks:
            nouns.append(tok.text)

        if len(nouns) == 0:
                newpositivelist = positivelist1
        else:
            for positive in positivelist2:
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