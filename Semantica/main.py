from flask import Flask, render_template

#parametros de inicialização

app = Flask(__name__)

@app.route('/ex1a')
def ex1a():
    return render_template('ex1a.html')

@app.route('/ex1b')
def ex1b():
    return render_template('ex1b.html')

@app.route('/ex2a')
def ex2a():
    return render_template('ex2a.html')

@app.route('/ex2b')
def ex2b():
    return render_template('ex2b.html')

@app.route('/ex2c')
def ex2c():
    return render_template('exe2c.html')

@app.route('/ex2d')
def ex2d():
    return render_template('exe2d.html')

@app.route('/ex3a')
def ex3a():
    return render_template('ex3a.html')

# Executar aplicação

app.run()


