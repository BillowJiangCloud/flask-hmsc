SERVER_PORT = 5000
SQLALCHEMY_DATABASE_URI = 'mysql://root:19970218@127.0.0.1/hmsc?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Cookie
AUTH_COOKIE_NAME = "hmsc_1901C"

# 设置拦截器忽略规则
IGNORE_URLS = ["^/user/login"]
IGNORE_CHECK_LOGIN_URLS = ["^/static", "^/favicon.ico"]

PAGE_SIZE = 2

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '\\web\\static\\upload',
    'prefix_url': '\\static\\upload'
}
