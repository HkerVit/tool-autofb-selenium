
from FBAuto import autofb


fb = autofb()
cookies = [{
    'name': 'c_user',
    'value': '100049316929620'
},
    {
    'name': 'datr',
    'value': 'CQeFXsqsH2coSt6qoYqPwsvK'
},
    {
    'name': 'fr',
    'value': '5hYVB75Gzohl5CRUX.AWXj9lqkQoKnkdDIcdes8mxCirk.BehQcJ.U6.AAA.0.0.BehQc2.AWXhENC4'
},
    {
    'name': 'sb',
    'value': 'ZVBRXnaVR1gQzuBxC1uptvUd'
},
    {
    'name': 'xs',
    'value': '5%3AzD_tEXdCFymYNA%3A2%3A1585776441%3A-1%3A-1'
}]

account = {
    'username': '100049606957207',
    'password': 'hoaihuynh9987',
    '2faSecret': 'DBQICDQHYD6QHBF3AEZ6QIMC7SKWAXCJ'
}
fb.login(account, 'account')

creditCard = {
    'cardName': 'DucEUMedia',
    'cardNumber': '4089051094993531',
    'cardExperied': '11/24',
    'ccv': '662'
}

fb.addCredit(creditCard)

