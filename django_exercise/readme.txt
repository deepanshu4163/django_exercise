you can find manage.py file in mydash directory

.venv is the hidden file in the base directory contains setting for virtual environment

#input was given
http POST http://127.0.0.1:8000/api/ Authorization:"token 9f744fe31bc67ab48ac5c31437f5916441e29fbd" message="api made from httpie"


#output

HTTP/1.1 200 OK
Allow: GET, POST, OPTIONS
Content-Length: 214
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 19 May 2022 14:04:03 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.10
Vary: Accept
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "created_by": {
        "email": "deepanshu@gmail.com",
        "user": "deepanshu",
        "user_id": "1"
    },
    "data": {
        "created_at": "2022-05-19T14:04:03.408632Z",
        "id": 6,
        "message": "api made from httpie",
        "updated_at": "2022-05-19T14:04:03.408659Z"
    }
}


#when input given with wrong token
http POST http://127.0.0.1:8000/api/ Authorization:"token f744fe31bc67ab48ac5c31437f5916441e29fbd" message="another api made from httpie"

#output

Allow: OPTIONS, POST, GET
Content-Length: 27
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 19 May 2022 14:38:43 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.10
Vary: Accept
WWW-Authenticate: Token
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Invalid token."
}


