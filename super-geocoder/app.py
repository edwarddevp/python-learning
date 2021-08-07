from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
from datetime import datetime
import pandas

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method != 'POST':
        return

    nom = Nominatim(user_agent='sample-email@gmail.com')

    file = request.files["file_input"]
    try:
        df = pandas.read_csv(file)
    except:
        return render_template('success.html', text="Ingrese un archivo .csv valido")

    address_name = ""
    if "Address" in df.columns:
        address_name = "Address"
    elif "address" in df.columns:
        address_name = "address"
    elif "ADDRESS" in df.columns:
        address_name = "ADDRESS"
    else:
        return render_template('success.html', text="El csv subido debe contener una columna Address de la cual se obtendran las coordenadas")

    coordinates = df[address_name].apply(nom.geocode)
    df["Latitude"] = coordinates.apply(
        lambda x: x.latitude if x != None else None)
    df["Longitude"] = coordinates.apply(
        lambda x: x.longitude if x != None else None)

    global filename
    filename = r'uploads/geocode_' + \
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f') + ".csv"
    df.to_csv(filename, index=False, header=True)

    rows = [
        {"Address": x, "Latitude": y, "Longitude": z}
        for x, y, z in zip(df["Address"], df["Latitude"], df["Longitude"])
    ]

    return render_template('success.html',
                           btn="download.html",
                           columns=["Address", "Latitude", "Longitude"],
                           rows=rows)


@app.route('/download')
def download():
    print("WTf")
    return send_file(filename, download_name="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
