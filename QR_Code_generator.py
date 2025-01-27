import qrcode

def QR(name,data):
 qr = qrcode.QRCode(
    version = 10,
    box_size = 10,
    border = 5,
 )	
 data = data
 name = name
 qr.add_data(data)
 qr.make(fit = True)
 img = qr.make_image(fill='black',back_color='white')    
 img.save(name+'.png')
 
QR("PARI","pari@1234")