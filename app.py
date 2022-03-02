from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True) #저장할때마다 변경된 것을 인식하고  다시 실행 함