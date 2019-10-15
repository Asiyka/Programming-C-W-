users=[
    {'username':'ladygaga','password':'supertop','birthday':'20.11.2006'},
    {'username':'asiyka01','password':'annansi','birthday':'02.01.2001'},
    {'username':'ludasosed','password':'zupagood','birthday':'4.6.1998'},
    {'username':'makaron02','password':'kotletka','birthday':'10.5.2011'}
]
username=(input('username:'))
password=(input('password:'))
message=""
for user in users:
    if username ==user['username']:
        if password==user['password']:
            message='You login'
            break
        else:
            message='Not correct password'
            break
    else:
        message='Not correct username'
        break
for date in users:
    if date['birthday'] <='15.10.2001':
        message='Ви увійшли!'
        break
    else:
        message='Вам менше 18!'
        break
print(message)
