# coding:utf-8
from flask import session, make_response, redirect, Flask, render_template, request, url_for
from geetestlib import GeetestLib

BASE_URL = "api.geetest.com/get.php?gt="
id = "a40fd3b0d712165c5d13e6f747e948d4"
key = "0f1a37e33c9ed10dd2e133fe2ae9c459"
product = "embed"

# 弹出式
# product = "popup&popupbtnid=submit-button"

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SERVER_NAME='127.0.0.1:5000'
)


@app.route('/getcaptcha', methods=["GET","POST"])
def get_captcha():
    gt =  GeetestLib(id, key)
    if gt.pre_process():
          res_str = gt.get_success_pre_process_res()
          session['server_status'] = 1
    else:
          res_str = gt.get_fail_pre_process_res()
          gt.set_gtserver_session(session, 0)
    print session
    return res_str

@app.route('/validate', methods=["GET","POST"])
def validate_capthca():
    gt = GeetestLib(id,key)
    print session
    gt_server_status = gt.get_gtserver_session(session)
    if gt_server_status == 1:
          result = gt.enhenced_validate_request(request)
    else:
          result = gt.failback_validate_request(request)
    return 'sucess'

@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = 'geetest233333333'
    app.run()