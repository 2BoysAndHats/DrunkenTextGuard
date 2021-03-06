import contextio as c
from bottle import route, run, template, get, post, request, redirect
import requests

#Login to context io
CONSUMER_KEY = 'nparu2by'
CONSUMER_SECRET = '3i5PIoxYuX9Y4lGK'
API_VERSION = '2.0' # "lite" or "2.0"

context_io = c.ContextIO(
  consumer_key=CONSUMER_KEY,
  consumer_secret=CONSUMER_SECRET,
  api_version=API_VERSION
)

#Signin route
@route("/signin")
def signin():
    dire = context_io.post_connect_token(callback_url="http://localhost:8080/redir",email=request.query.email)
    redirect(dire["browser_redirect_url"])

@route("/redir")
def redir():
    #Add webhook
    account = c.ConnectToken(context_io,{"token":request.query.contextio_token})
    account.get()
    aid = account.account.id
    account = account.account
    # account.post_webhook(callback_url="http://localhost:8080/webhook",failure_notif_url="http://localhost:8080/webhook_failure")
    account.post_webhook(callback_url="https://whitehat-a2boysandhats-1.c9users.io/webhook",failure_notif_url="https://whitehat-a2boysandhats-1.c9users.io/webhook_failure")

@route("/webhook")
def webhook():
    return ""

run(host="localhost", port=8080)
