# integrate html with flask >>> this is called jinja2 technique
#http verbs like a GET and POST

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return 'the student is passed and the marks is'+ str(score)
    
@app.route('/fail/<int:score>')
def fail(score):
    return 'the student is failed and the marks is'+ str(score)
    # return f"The student is failed and the marks is {score}"

# result checker

@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks<24:
        result ='fail'
    else:
       result ='success'
    # return result
    return redirect(url_for(result,score=marks))


# result checker submit html File

@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        Java = float(request.form['Java'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (Java+maths+c+data_science)/4

    res=""
    if total_score >= 50:
        res='success'
    else:
        res = 'fail'

    return redirect(url_for(res,score=total_score))


if __name__=='__main__':
    app.run(debug=True)
