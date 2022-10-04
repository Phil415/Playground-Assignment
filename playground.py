from flask import Flask, render_template, url_for  # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/play/')
@app.route('/play/<count>/')
@app.route('/play/<count>/<color>/')
def play(count="3", color="#9ec5f8"):
    return render_template('playground.html', count=int(count), color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
#this is always at the bottom