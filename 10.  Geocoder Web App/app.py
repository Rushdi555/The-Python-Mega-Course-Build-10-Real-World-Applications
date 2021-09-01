from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas
from io import StringIO
from geopy.geocoders import ArcGIS
nom = ArcGIS(timeout = 10) 

app=Flask(__name__)       

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        bytes_data=file.read()
        s=str(bytes_data,'utf-8')
        data = StringIO(s) 
        df1=pandas.read_csv(data)
        if 'Address' in df1.columns:
            df1["Coordinates"]=df1["Address"]. apply(nom.geocode)
            df1["Latitude"]=df1['Coordinates'].apply(lambda x: x.latitude if x != None else None)
            df1["Longitude"]=df1['Coordinates'].apply(lambda x: x.longitude if x != None else None)
            del df1['Coordinates']
            df1.to_csv("upload/converted "+file.filename, index=False)
            return render_template("index.html", btn="download.html", tables=[df1.to_html(classes='data')])
        elif 'address' in df1.columns:
            df1["Coordinates"]=df1["address"]. apply(nom.geocode)
            df1["Latitude"]=df1['Coordinates'].apply(lambda x: x.latitude if x != None else None)
            df1["Longitude"]=df1['Coordinates'].apply(lambda x: x.longitude if x != None else None)
            del df1['Coordinates']
            df1.to_csv("upload/converted "+file.filename, index=False)
            return render_template("index.html", btn="download.html", tables=[df1.to_html(classes='data')])
        else:
            return render_template("index.html", text="Upload a csv file with Address column")

@app.route("/download")
def download():
    return send_file("upload/converted "+file.filename, attachment_filename="Coordinates "+file.filename, as_attachment=True)

if __name__=='__main__':
    app.debug=True
    app.run()