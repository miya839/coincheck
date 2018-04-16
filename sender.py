#!/usr/bin/python
#-*- codong: utf-8 -*- 

import requests

class Line:
    def __init__(self):
        self.line_notify_token = 'address'
        self.line_notify_api = 'https://notify-api.line.me/api/notify'

    def sender(self, message):
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + self.line_notify_token}
        line_notify = requests.post(self.line_notify_api, data=payload, headers=headers)

if __name__ == '__main__':
    Line().sender("test")
    


