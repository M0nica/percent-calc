from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('entry.html')

@app.route("/entry", methods=['POST'])
def calculate():
    original_number = request.form['original']
    new_number = request.form['new']
    result = ((int(new_number) - int(original_number))/int(original_number)) * 100
    response =  "The percent change between " + original_number + " and " + new_number + " is " + str("%.0f%%" % result)


    return render_template('result.html',
                           response = response)

if __name__ == '__main__':
    app.run(debug=True)
