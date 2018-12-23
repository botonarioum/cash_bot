from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook/<token>')
def webhook_endpoint(token):
    # if request.method == 'POST':
    #     return do_the_login()
    # else:
    #     return show_the_login_form()
    return 'webhooks here {}'.format(token)


if __name__ == '__main__':
    app.run()
