from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # แสดงหน้าแรกที่มีปุ่ม Yes / No
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
  
