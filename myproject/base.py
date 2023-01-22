from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Two Dollar Holla'
    stuff = 'This one is <strong>Tuff</strong> Nwanne'
    items = ['item 1', 'item 2', 'item 3']
    return render_template('base.html',
                           title=title,
                           items=items,
                           stuff=stuff
                           )

if __name__ == '__main__':
    app.run()

@app.route('/user/<name>')
def user(name):
    designer = ["Versace", "Dior", "GUCCI", 19]
    title = 'Three Dollar Holla'
    return render_template("hello.html",
                           username= name,
                           title= title,
                           designer= designer
                           )
    
@app.route("/work")
def work():
    title = 'Defined'
    joy = "Everywhere"
    items = ['item 1', 'item 2', 'item 3']
    stuff =  "New Things"
    return render_template("work.html",
                           joy=joy,
                           title=title,
                           items=items,
                           stuff=stuff)