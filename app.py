from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
import time


def validate_email_addresses(email):
    import requests

    email_address = email
    try:
        response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params={'email': email_address}, timeout=5)

        status = response.json()['status']
        if status == "valid":
            print("email is valid")
            output = True
        elif status == "invalid":
            output = False
        else:
            print("email was unknown")
            output = False
    except:
        output = False
    output = "Email address {} is shown to be {}".format(email,output)
    print(email, output)
    return output

def btn_click(btn_val):
    if btn_val == 'New Email':
        output = True
    else:
        output = False
    return output


@use_scope('time', clear=True)
def show_email_validate_output(email_address):
    put_text('Checking email address...')
    output = validate_email_addresses(email_address)
    put_processbar('bar')
    for i in range(1, 6):
        set_processbar('bar', i / 5)
        time.sleep(0.1)
    put_text("\n\n")

    put_text(output)

def app():
    put_text("DISCLAIMER. \n\nA third party API is being utilised and hence we can not provide 100% certainty on email validation technique used.\nAll information is stored securely.")
    while output:
        email_address = input("What is the email address you would like to check?", required=True)
        show_email_validate_output(email_address)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(app, port=args.port)
#if __name__ == '__main__':
    #predict()

#app.run(host='localhost', port=80)

#visit http://localhost/tool to open the PyWebIO application.