from twilio.rest import Client

import config

client = Client(config.account_sid, config.auth_toeken)

call = client.calls.create(
    to=config.destination_number,
    from_=config.source_number,
    url="https://demo.twilio.com/welcome/voice/",
)
