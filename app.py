from flask import Flask
from flask import render_template
from flask import jsonify
#flask is module that describes the framework used to design web applications in python
#template means page formatting in this instance
#Render is the proccess of creating/showing a page in this case
#Rendering is the creation of a visual representation
#The HTML File will contain all the infomation that will be shown
# CSS Cascading style sheets is a programme used to add style and presentation to a web page 
# HTML is a programming language used to design and create a web pages

i =[{'1': "Data Analyst","2":"Johannesburg","3":30000,"4":"Immediate","info": "We looking for a Data Analyst that is very eager and enthusiastic about analysing Data."},{'1':"Programmer","2":"Pretoria","3":20000,"info":"We looking for a Phython Programmer with execellent computing skills and great ambition"},]

cyber = Flask(__name__)

@cyber.route("/")
def cyberUniverse():
  return render_template("bootstrap.html", jobs=i)
#JSON database route, JSON stands for JavaScript Object Notation and it is a file format and it is used for transmitting data in web applications 
@cyber.route("/api/jobs")
def joblist():
  return jsonify(i)
  
if __name__ == "__main__":
  cyber.run(host="0.0.0.0",debug=True)

