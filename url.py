#building url dynamicall 


from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'url building'

@app.route('/success/<int:score>')
def success(score):
    return 'the student is passed and the marks is'+ str(score)
    
@app.route('/fail/<int:score>')
def fail(score):
    return 'the student is failed and the marks is'+ str(score)
    # return f"The student is failed and the marks is {score}"


@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks<24:
        result ='fail'
    else:
       result ='success'
    # return result
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)
