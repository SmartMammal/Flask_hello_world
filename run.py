from flask import Flask, render_template # import the flask class and render_template
app = Flask(__name__) # create an instance of the class "app" passing __name__

#This function returns the string... Hello World
@app.route("/hello") # app.route decorator: when the user visits the specified URL, run the function
def hello_world():
    return render_template('template.html', salutation="World!")

#This function returns the string... Hello <namehere>
@app.route("/hello/<name>") # Second view
def hello_personal(name):
    return render_template('template.html', salutation=name.title() )

#This function returns the string... Hello <jediname>
@app.route("/jedi/<fname>/<lname>")
def hello_jedi(fname, lname):
    jediname = str(lname[:3]+fname[:2])                     
    return render_template('template.html', salutation="and aloha {}!".format( jediname.title() ) )

                           
if __name__ == "__main__": # Main block
    app.run(host="0.0.0.0", port=8080) #run the application; use the host and port arguments to tell the application to listen on a port which can access through Nitrous.IO


