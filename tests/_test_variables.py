import os

# BROWSER OPTIONS: firefox, headlessfirefox, chrome, headlesschrome
BROWSER = os.environ.get("BROWSER").lower() if os.environ.get("BROWSER") else "headlessfirefox"
DRIVER_LOGS = ".logs/geckodriver.log" if BROWSER in ["firefox", "headlessfirefox"] else None
OPTIONS = None
TIMEOUT = os.environ.get("TIMEOUT") or 20


# PORTS
PORT_LOGOUT_NAME_CHANGE = 8008
PORT_HIDE_MENU = 8007
PORT_HIDE_FOOTER = 8006
PORT_CUSTOM_USER_STORAGE = 8009
PORT_CUSTOM_LOGIN_NAME = 8005
PORT_CUSTOM_AUTH_NO_ACCOUNT_MGMT = 8004
PORT_HIDE_ACCOUNT_MGMT = 8003
PORT_HIDE_REGISTRATION = 8002
PORT_DEFAULT_JSON = 8001
PORT_CUSTOM_FORGOT_PASSWORD = 8010
PORT_CUSTOM_AUTH_COOKIES = 8011
PORT_MULTIPAGE_AUTH = 8013
PORT_DEFAULT_SQLITE = 8014
PORT_DEFAULT_POSTGRES = 8015
PORT_INIT_SQLITE_STORAGE = 9999
PORT_INIT_POSTGRES_STORAGE = 9998
