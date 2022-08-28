from flask import Flask, jsonify, request
import csv
allArticles = []
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]
likedArticles = []
notLikedArticles = []
app = Flask(__name__)
@app.route('/get-article')
def getArticle():
    return jsonify({
        'data': allArticles[0],
        'status': 'success'
    })
@app.route('/liked-article', methods = ['POST'])
def likedArticle():
    article = allArticles[0]
    likedArticles.append(article)
    allArticles.pop(0)
    return jsonify({
        'status': 'success'
    }), 201
@app.route('/unliked-article', methods = ['POST'])
def unlikedArticle():
    article = allArticles[0]
    notLikedArticles.append(article)
    allArticles.pop(0)
    return jsonify({
        'status': 'success'
    }), 201
if __name__ == '__main__':
    app.run()