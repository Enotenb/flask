from flask import Flask, request

from flask.utils import get_password, requirements_return, get_fake, astronavt_get, average_all

app = Flask(__name__)


@app.route('/password')
def password():
    length = request.args.get('length') or '10'

    if length.isdigit():
        length = int(length)
        max_length = 200

        if length > max_length:
            return f'Max length should be less that {max_length}.'
    else:
        return f'Invalid parameter length {length}. Integer is expected.'

    result = get_password(length)
    return result


@app.route('/requirements/')
def requirements():
        return requirements_return()

@app.route('/generate-users/')
def generate():
    quantity = request.args.get('quantity', '100')

    if quantity.isdigit():
        quantity = int(quantity)
    else:
        return f'Integer is expected'

    result = get_fake(quantity)
    return result

@app.route('/space/')
def astronavt():
    return astronavt_get()

@app.route('/average/')
def average():
    return average_all()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

'''
http:// 172.27.201.140 :5000 / ?length=20&name=Dima&age=30
1       2                 3  4  5

1. protocol
   http:// https:// ftp:// (filezilla) smtp:// amqp://

2. Destination. Domain, IPv4, IPv6
IPv4
0-255.0-255.0-255.0-255
0.0.0.0 - yes
254.0.0.1 - yes
254.0.0.0.1 - no
254.0.1 - no

localhost - 127.0.0.1

3. Port - 0 - 65_535
0 - root
80 - http
443 - https

4 Path

5 Query string
'''

