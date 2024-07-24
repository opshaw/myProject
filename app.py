from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/breast-cancer')
def BreastCancer():
    return render_template('BreastCancer.html')

@app.route('/covid-19')
def Covid19():
    return render_template('Covid19.html')

@app.route('/diabetes')
def Diabetes():
    return render_template('Diabetes.html')

if __name__ == '__main__':
    app.run(debug=True)
