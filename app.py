from flask import Flask, render_template, send_file
from ftplib import FTP
import os

app = Flask(__name__)

# Definir directorio de descargas
DIRECTORIO_DESCARGAS = 'downloads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar')
def enviar():
    return render_template('enviar.html')

@app.route('/crearpdf')
def crearpdf():
    return render_template('crearpdf.html')

@app.route('/SweetAlerts')
def sweet_alerts():
    return render_template('SweetAlerts.html')

@app.route('/descargar')
def descargar():
    return render_template('descargar.html')

@app.route('/descargar/archivo')
def descarga_archivo_ftp():
    ftp = FTP()
    ftp.connect('ftpupload.net')
    ftp.login(user='b18_35964124', passwd='134340Ko!')

    archivo_ftp = 'PruebaTxt.txt'
    ruta_descarga = os.path.join(DIRECTORIO_DESCARGAS, archivo_ftp)  
    with open(ruta_descarga, 'wb') as archivo_local:
        ftp.retrbinary('RETR ' + archivo_ftp, archivo_local.write)
    ftp.quit()

    return send_file(ruta_descarga, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
