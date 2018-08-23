URL = "http://static1.keepcdn.com/picture/2018/08/21/17/95f2c56681d7cbd6791a3ec8fcc385231f80d937_960x540.jpg?imageMogr2/thumbnail/306x/quality/95"
import requests
import re

# try:
#     pic = requests.get(URL)
#     with open("pic.jpg", 'wb') as f:
#         f.write(pic.content)
# except Exception as e:
#     print(repr(e))

pattern = re.compile(r'"(htt.*jpg.*) class|(htt.*jpg.*)\)"')
res = pattern.finditer(
    '''
    '<div class="img"><div data-background="http://static1.keepcdn.com/picture/2018/07/15/20/f09a562a22592fab1ef598517eb04ca222832e9a_1335x1334.jpg?imageMogr2/thumbnail/306x/quality/95" class="keep-lazy"></div></div>'
    ''')
for item in res:
    print(item.group())