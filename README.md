# amazon_auth
A Python tool to generate and refresh Amazon access tokens.

## Description

This tool generates and outputs Amazon access and refresh tokens for a given email and password pair for a specific Amazon domain. The tokens are also stored to allow refreshing instead of regenerating later on. The generated tokens can be used to access APIs for different Amazon services such as Prime Video, ComiXology, Audacity, and e.t.c.

## Installation

0. Make sure that you have Python 3 installed before installing this tool
1. Clone the tool using `git clone https://github.com/athrowaway2021/amazon_auth` or download the source code as a zip and unpack it in any location.
2. Install libraries required by the tool using `pip install -r requirements.txt`

## Usage

To use this tool, provide it with an email, password, and the domain of the API. Some services, such as ComiXology, do not care about which domain you chose for the token, whereas, Prime Video, for example, will limit what content you can access based on the token. The process may fail if you are using a detected VPN or aren't in one of the domains' countries. Additionally, make sure you are able to login from the browser to prevent OTP related issues.

```
> python amazon_auth.py [email] [password] com
{"domain": "com", "access_token": "Atna|[redacted]", "refresh_token": "Atnr|[redacted]"}
```

## Third-Party
This program uses the Python standard library and the following:
  - [requests](https://github.com/psf/requests)

See `/licenses/` for the corresponding licenses, copyright notices, and permission notices.
