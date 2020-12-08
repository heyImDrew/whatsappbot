from twilio.rest import Client

account_sid = 'AC30610c7063f209eefaa1736dde4ead68'
auth_token = '207f0023b18d7db10e5c83b4f4abcdc4'
client = Client(account_sid, auth_token)

message = input()

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=message,
    to='whatsapp:+375447810315'
)
