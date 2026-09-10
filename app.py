from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "helloworlddddd devopsss lab"
if __name__=='__main__':
    app.run(debug=True)
