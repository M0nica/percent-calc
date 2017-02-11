from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def hello():
    return render_template('entry.html')

@app.route("/entry", methods=['POST'])
def calculate():
    original_number = float(request.form['original'])
    new_number = float(request.form['new'])

    result_unf = float((new_number - original_number)/(original_number))

    # response =  "The percent change between " + str(original_number) + " and " + str(new_number) + " is " + str("{:.2%}".format(result))
    result = str("{:.2%}".format(result_unf))

    return render_template('result.html',
                           x=int(original_number),y=int(new_number),result=result)



if __name__ == '__main__':
    app.run(debug=True)
