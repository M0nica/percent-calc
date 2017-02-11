from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def hello():
    return render_template('entry.html')

@app.route("/entry", methods=['POST'])
def calculate():
    original_number = int(request.form['original'])
    new_number = int(request.form['new'])



    # return render_template('result.html',
    #                        x=int(original_number),y=int(new_number),result=result)

    return redirect(url_for('results', x=original_number,y=new_number))


@app.route('/results/<x>/<y>')


def results(x, y):
    x = float(x)
    y = float(y)

    result_unf = float((x-y)/(y))

    # response =  "The percent change between " + str(original_number) + " and " + str(new_number) + " is " + str("{:.2%}".format(result))
    result = str("{:.2%}".format(result_unf))
    return render_template('results.html', x=x,y=y,result=result)

if __name__ == '__main__':
    app.run(debug=True)
