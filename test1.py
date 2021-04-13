from flask import Flask

app = Flask(__name__)

@app.route("/") #装饰器加括号和不加括号区别
def index():
    return "hello world"

if __name__=='__main__':
    app.run()
    #请求来了，执行 app(request), 会触发 __call__方法