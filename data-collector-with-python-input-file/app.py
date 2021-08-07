from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method != 'POST':
        return
    global file
    file = request.files["file_input"]
    file.save(secure_filename("uploaded_" + file.filename))
    with open("uploaded_" + file.filename, "a") as f:
        f.write("This was add later")
    return render_template('index.html', btn="download.html")


@app.route('/download')
def download():
    return send_file("uploaded_" + file.filename,
                     attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
