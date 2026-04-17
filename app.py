from flask import Flask

app = Flask(__name__)

# decorator
@app.route('/')
def welcome():
    return 'hello Flask,this is divyanshu kumar'
    
@app.route('/intro')
def intro():
    return 'hello Flask,i am divyanshu'

if __name__=='__main__':
    app.run(debug=True)












