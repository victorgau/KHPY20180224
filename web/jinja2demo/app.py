from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "這是 jinia2 的測試"
    fruits = ['apple', 'orange', 'grape']
    return render_template('index.html', title=title, fruits=fruits)

if __name__=="__main__":
    app.run()
