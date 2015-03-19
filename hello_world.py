from flask import Flask # import the flask class

app = Flask(__name__) # create an instance of the class "app" passing __name__

@app.route("/hello") # app.route decorator: when the user visits the specified URL, run the function
def hello_world():
    return "Hello World!" #The function returns the string... Hello World

#@app.route("/hello/<name>") # Second view
#def hello_person(name):
#    return "Hello {}!".format(name.title())


@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
 
@app.route("/jedi/<fname>/<lname>")
def hello_jediperson(lname, fname):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    
    jediname = str(lname[:3]+fname[:2])
    
    return html.format(jediname.title())
 
if __name__ == "__main__": # Main block
    app.run(host="0.0.0.0", port=8080) #run the application; use the host and port arguments to tell the application to listen on a port which can access through Nitrous.IO


