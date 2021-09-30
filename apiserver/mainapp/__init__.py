from flask import Flask
from flask import render_template
app = Flask(__name__)



# 捕获异常
@app.errorhandler(404)
def notfound(error):
    return render_template('404.html')