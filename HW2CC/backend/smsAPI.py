from twilio.rest import Client


def send_message(m):
    account_sid = "AC63c63c7127b7984b4f7006ee4765ec32"
    auth_token = "d40c7faf78a858c2ff775baaf8a9eb5f"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=m,
        from_="+15076074303",
        to="+40745428411"
    )
    print(message.sid)