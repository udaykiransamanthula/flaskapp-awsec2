from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '<h1> This is udaykiran</h1><br><p>Thank you . this is second time i told to bintu  I hope you enjoyed it, follow for more content around Devops.</p> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
