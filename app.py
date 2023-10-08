from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("index.html")

@app.route("/calculate", methods=["post"])
def calculate():
  first_number = int(request.form["firstNumber"])
  operation = request.form["operation"]
  second_number = int(request.form["secondNumber"])
  if operation == "plus":
    result = first_number + second_number
  elif operation == "minus":
    result = first_number - second_number
  elif operation == "divide":
    result = first_number / second_number
  elif operation == "multiply":
    result = first_number * second_number
  else:
    return "This is an error, please try again"
  return render_template("calculator.html", result=result)


if __name__=="__main__":
  app.run(port=5000, debug=True)