from flask import Flask,render_template,request,send_from_directory,send_file,Response # type: ignore
import qrcode
import io

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def qrc():
    if request.method == 'GET':
        return render_template('qr.html')
    if request.method == 'POST':
        name = request.form.get('name')
        link = request.form.get('link')
        location = request.form.get('location')
        qr = qrcode.QRCode(version = 10, box_size = 10,border = 5)
        if location:
            lat, lng = location.split(',')
            here_link = f'https://share.here.com/l/{lat},{lng}'
            qr.add_data(here_link)
        elif link:
            qr.add_data(link)
        else:
            return 'No link or location provided', 400
        qr.make(fit = True)
        img = qr.make_image(fill='black',back_color='white')  
        ni = io.BytesIO() 
        img.save(ni,'PNG')
        ni.seek(0)
        nn = name+'.png'
        return send_file(ni,mimetype='image/png',as_attachment=True,download_name = nn)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
