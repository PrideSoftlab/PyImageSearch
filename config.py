import os

BOT_NAME = os.environ.get("BOT_NAME", "PyImageSearch")
CSE_KEY = os.environ.get("CSE_KEY", "AIzaSyABz7ZDCq_bxyMKn8Q2Y45jcpBcnliV0p8")
CSE_CX = os.environ.get("CSE_CX", "")
API_TOKEN = os.environ.get("API_TOKEN", "520108577:AAGrI42bl5WVgH0kP2-ZBILXGhwwJX9Umtc")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")
NGINX_SUBPATH = os.environ.get("NGINX_SUBPATH", "")
BATCH = int(os.environ.get("BATCH", 10))
POLLING = bool(os.environ.get("POLLING", False))