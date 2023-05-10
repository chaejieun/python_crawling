import requests

token = "xoxb-5241687466274-5241883088403-Jg6gp5AKXUoJtXtgygVdnYT4"
channel = "#개인"
text = "파이썬 크롤링 슬랙봇입니다"

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})