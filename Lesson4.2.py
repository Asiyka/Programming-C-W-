users=[
    {'username':'ladygaga','password':'supertop'},
    {'username':'asiyka01','password':'annansi'},
    {'username':'ludasosed','password':'zupagood'},
    {'username':'makaron02','password':'kotletka'}
]
username=(input(':'))
password=(input(':'))
for user in users:
    if username ==user['username']:
        if password==user['password']:
            flag='You login'
            break
        else:
            flag='Not correct password'
            break
    else:
        flag='Not correct username'
        break
print(flag)
