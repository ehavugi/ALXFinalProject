from json import dumps

from httplib2 import Http

# https://developers.google.com/chat/how-tos/webhooks
WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAAAH4auljs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=wDo3fcTQXPCgNHKQwzagCkNJr7tTXLJHNUaJVS9scs4"
def notify_msg(msg, WEBHOOK_URL=WEBHOOK_URL):
    """Google Chat incoming webhook quickstart."""
    url = WEBHOOK_URL
    app_message = {
        'text': msg}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


if __name__ == '__main__':
    notify_msg('Hello there!')
