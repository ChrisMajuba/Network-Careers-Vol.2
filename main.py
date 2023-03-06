from flask import Flask
from flask import render_template
#flask is module that describes the framework used to design web applications in python
#template means page formatting in this instance
#Render is the proccess of creating/showing a page in this case
#The HTML File will contain all the infomation that will be shown
# CSS Cascading style sheets is a programme used to add style and presentation to a web page 
# HTML is a programming language used to design and create a web pages
app = Flask(__name__)

@app.route("/")
def cyberUniverse():
  return render_template("bootstrap.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)

