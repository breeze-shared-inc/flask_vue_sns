from flask import Flask, render_template
# flaskインスタンス生成
app = Flask(__name__)

# モノリシックなアプリ
# htmlのテンプレートの呼び出し
# API

#h1タグのしたにpタグ Hello {{name}} .
@app.route('/<name>')
def hello(name):
  return render_template("hello.html", name=name)

#h1タグのしたにpタグ Good {{good}} .
@app.route('/good/<name>')
def good(name):
    return render_template("good.html", name=name)

#h1タグのしたにpタグ Good {{good}} .
@app.route('/ken/<name>/<style>')
def len(name,style):
    return render_template("ken.html", name=name,style=style)

app.run(debug=True)