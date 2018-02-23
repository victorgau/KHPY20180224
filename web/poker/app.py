from flask import Flask, render_template, request
import random

app = Flask(__name__)

numbers = range(1, 14)
colors = ['S', 'H', 'C', 'D']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            guess = request.form['submit']
        except Exception as e:
            guess = ""
            print('Error occurs:', e.args)
        
        color = random.choice(colors)
        number = random.choice(numbers)
        poker = color + str(number)

        if number > 7:
            if guess=='大':
                result = '你贏了！'
            else:
                result = '你輸了！'
        elif number < 7:
            if guess=='小':
                result = '你贏了！'
            else:
                result = '你輸了！'
        else:
            result = '平手！'

        return render_template('index.html', result=result, poker=poker)

    elif request.method == 'GET':
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)