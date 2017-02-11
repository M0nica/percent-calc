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

    result_unf = float((y-x)/(x))

    # response =  "The percent change between " + str(original_number) + " and " + str(new_number) + " is " + str("{:.2%}".format(result))
    result = str("{:.2%}".format(result_unf))
    return render_template('results.html', x=int(x),y=int(y),result=result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
