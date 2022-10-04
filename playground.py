from flask import Flask, render_template, url_for  # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/play/<count>/<color>/')
def play(count, color):
    return render_template('playground.html', count=int(count), color=color)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
#this is always at the bottom

"""
@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<insertword>')
def say(insertword):
    print(insertword)
    return f"Hi {insertword}!"

@app.route('/repeat/<int:insertnumber>/<insertword>')
def repeat(insertnumber, insertword):
    print(insertnumber, insertword)
    return insertword * insertnumber
"""