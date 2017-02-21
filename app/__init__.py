from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def hello():
    return render_template('entry.html')

@app.route("/entry", methods=['POST'])


def calculate():
    original_number = format(request.form['original'])
    new_number = format(request.form['new'])
    return redirect(url_for('results', x=original_number,y=new_number))


def format(num):
    try:
        # only return an int if there is no decimal in the number
        return int(num)
    except ValueError:
        # if there is a decimal in the number then return the floating point
        return float(num)

@app.route('/results/<x>/<y>')


def results(x, y):


    result_unformatted = float((float(y)-float(x))/float(x))
    x = format(x)
    y = format(y)

    # response =  "The percent change between " + str(original_number) + " and " + str(new_number) + " is " + str("{:.2%}".format(result))

    # xx.xx% formatted string of percent change
    result = str("{:.2%}".format(result_unformatted))


    return render_template('results.html', x=x,y=y,result=result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html'), 404

if __name__ == '__main__':
    app.run(debug=False)
