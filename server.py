from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# # render 3 blue boxes
# @app.route('/play')
# def play():
#     return render_template('index.html')

# # render 'num' number of squares
# @app.route('/play2/<int:num>')
# def play2(num):
#     return render_template('index.html', num=num)

# render 'num' number of squares
@app.route('/play3/<int:num>/<string:color>')
def play3(num, color):
    return render_template('index.html', num=num, color=color)


# # SENSI BONUS (does not work)
# @app.route('/play/<int:num>/<string:color>')
# def play(num = 3, color = "dodgerblue"):
#     return render_template('index.html', num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

