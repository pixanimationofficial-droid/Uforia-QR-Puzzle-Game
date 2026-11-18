# Bikin QR polos + poster QR retro untuk alamat game.
# Pakai: pip install qrcode pillow fonttools brotli
#        python3 tools/qrposter.py https://alamat-game-kamu/
# Hasil: qr/UFORIA-QR.png dan qr/UFORIA-QR-poster.png
import sys, os
import qrcode
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
if len(sys.argv) < 2: sys.exit('Pakai: python3 tools/qrposter.py https://alamat-game/')
URL=sys.argv[1]
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(ROOT,'qr'),exist_ok=True); os.makedirs('/tmp/uforia-fonts',exist_ok=True)
for n in ['bungee','outfit-800']:
    f=TTFont(os.path.join(ROOT,'public/a/f',n+'.woff2')); f.flavor=None; f.save(f'/tmp/uforia-fonts/{n}.ttf')
q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=2)
q.add_data(URL); q.make(fit=True)
qr=q.make_image(fill_color=(22,19,61),back_color=(253,236,200)).convert('RGB'); qr.save(os.path.join(ROOT,'qr/UFORIA-QR.png'))
W,H=1080,1350
navy=(22,19,61); cream=(253,236,200); pink=(255,79,154); teal=(51,211,201); yellow=(255,200,58)
bg=Image.open(os.path.join(ROOT,'public/a/bg.webp')).convert('RGB')
bg=bg.resize((int(bg.width*H*0.55/bg.height),int(H*0.55)))
P=Image.new('RGB',(W,H),navy); P.paste(bg,((W-bg.width)//2,0))
grad=Image.new('L',(1,H))
for y in range(H): grad.putpixel((0,y),int(max(0,min(255,(y-H*0.25)/(H*0.3)*255))))
P=Image.composite(Image.new('RGB',(W,H),navy),P,grad.resize((W,H)))
d=ImageDraw.Draw(P)
for y in range(int(H*0.5),H,18):
    for x in range(0,W,18): d.ellipse((x,y,x+2,y+2),fill=(60,52,110))
logo=Image.open(os.path.join(ROOT,'public/a/uforia.webp')).convert('RGBA'); lw=580; logo=logo.resize((lw,int(lw*logo.height/logo.width)),Image.LANCZOS)
P.paste(logo,((W-lw)//2,30),logo)
fb=lambda s:ImageFont.truetype('/tmp/uforia-fonts/bungee.ttf',s); fo=lambda s:ImageFont.truetype('/tmp/uforia-fonts/outfit-800.ttf',s)
def ctext(y,txt,font,fill,shadow=None):
    w=d.textlength(txt,font=font); x=(W-w)/2
    if shadow:
        for i,c in enumerate(shadow): d.text((x+4*(i+1),y+4*(i+1)),txt,font=font,fill=c)
    d.text((x,y),txt,font=font,fill=fill)
ctext(272,'SCAN & MAIN!',fb(72),cream,[pink,teal])
ctext(368,'Mini game 15 detik · Salah Kostum!',fo(34),yellow)
qs=540; qri=qr.resize((qs,qs),Image.NEAREST); qx=(W-qs)//2; qy=478
for i,c in enumerate([yellow,teal,pink]):
    o=36-i*10; d.rounded_rectangle((qx-o,qy-o,qx+qs+o,qy+qs+o),radius=36,fill=c)
d.rounded_rectangle((qx-8,qy-8,qx+qs+8,qy+qs+8),radius=26,fill=cream)
P.paste(qri,(qx,qy))
ctext(1100,'31 DESEMBER 2026',fb(54),yellow)
ctext(1176,'CHASE PLAZA · SUDIRMAN, JAKARTA',fb(34),teal)
ctext(1246,'RAN · ADRIAN KHALIF · THE ANGELS · DJ THROOPER',fo(28),cream)
P.save(os.path.join(ROOT,'qr/UFORIA-QR-poster.png')); print('QR untuk',URL,'tersimpan di qr/')
