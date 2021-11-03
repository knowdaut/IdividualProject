from flask import Flask, render_template

app = Flask(__name__)  

@app.route("/")                
def hello():                    
    return render_template("index.html") 

@app.route("/potter")                
def potter():                    
    return render_template("potter.html") 

@app.route("/page3")                
def page3():                    
    return render_template("page3.html") 




if __name__ == "__main__":
    app.run(debug=True) 