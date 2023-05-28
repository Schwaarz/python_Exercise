import base64

from faker import Faker


fake = Faker(locale='zh_CN')



name = fake.name()
adds = fake.address()
text = fake.text()
email = fake.company_email()
phone = fake.phone_number()
print(fake.city())
print(fake.province())
print(fake.street_address())
print(name+' '+adds+ ' '+email+ ' ' +phone)
print(fake.pystr(min_chars=5, max_chars=8))
strInput="122221121122"
bs=str(base64.b64encode(strInput.encode('utf-8')),"utf-8")
print('转码：'+bs)
print('解码：'+str(base64.b64decode(bs),"utf-8"))






