from flask import Flask, render_template, request
import gacha_simulator  # ここでgacha_simulator.pyをインポート

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'pull_once' in request.form:
            result = gacha_simulator.pull_gacha(1)
        elif 'pull_ten_times' in request.form:
            result = gacha_simulator.pull_gacha(10)
        elif 'reset' in request.form:
            gacha_simulator.reset()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)