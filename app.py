from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    
    color = {
        'blue': '002aff',
        'yellow': 'e1eb34',
        'green': '28fc03',
        'red': 'fc1703', 
        'purple': 'b503fc'}
    
    return render_template('index.html', color=color)
    


@app.route('/register')
def register():
    return 'Please register!'

@app.route('/login')
def login():
    return 'Please login!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')