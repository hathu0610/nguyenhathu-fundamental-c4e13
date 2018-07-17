from gmail import GMail, Message
import random
from datetime import datetime, timedelta
import time,threading
gmail = GMail('hathu0610@gmail.com','tuantran1995')



html_content = """
<p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa việt nam</p>
<p style="text-align: center;">Độc lập - Tự Do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<h2 style="text-align: center;"><span style="color: #ff99cc;"><strong>ĐƠN XIN NGHỈ HỌC</strong></span></h2>
<p><em>Gửi thầy,</em></p>
<p>&nbsp;</p>
<p><em>H&ocirc;m nay em nghỉ học do {{sickness}} <img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-cool.gif" alt="cool" />. Xin thầy cho ph&eacute;p e nghỉ.<img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></em></p>
<p>&nbsp;</p>
<p>Thu</p>
"""
ly_do = ["em thích nghỉ", "em chán học", "cần đi uống trà sữa"]
html_tosend = html_content.replace("{{sickness}}", random.choice(ly_do))
msg = Message("Em nghỉ", to= 'hathu0610@gmail.com', html =html_tosend)

loop = True

while loop:
    now = datetime.now()
    if now.hour == 15:
        gmail.send(msg)
        break
    