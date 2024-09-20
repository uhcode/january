# Name: January API
# Description: A fast, secure & open source API for anyone to use.
# Author: uhcode
# Github: https://github.com/uhcode/january
# License: MIT


import uvicorn

from api import api

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=5000, log_level="info")