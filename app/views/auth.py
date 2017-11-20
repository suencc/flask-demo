import jwt
import time

from flask import render_template, request, jsonify, abort
from app import db, app
from app import front, apiv1bp
from app.model import demo


@front.route('create')
def create():

    """
    数据库创建
    :return: 
    """
    db.create_all()

    return "create ok"

@front.route('drop')
def drop_all():
    abort(500)
    """
    数据库清空
    :return: 
    """
    db.drop_all()
    return "drop ok"

@front.route('add_token_user/<username>/<password>')
def add_token_user(username, password):
    """
    
    :param username: 用户名
    :param password: 密码
    :return: 创建用户
    """
    user = demo.User(username=username, password=password)
    db.session.add(user)
    # db.session.commit()

    return "create : "+username

@front.route('rollback')
def rollback():
    """
    事务测试
    :return: 
    """
    user = demo.User(username="r", password="r")
    p = demo.Person(name="sfdsafdsasdfasfsdfsadfdsfsdfsdafwearfewfsfdfvxzvcxbvfvbdffdgafdsafsdafdfzxvdsfdfdsafdsgdfafxvcxvdsafdgfdafgsdf")
    db.session.add(user)
    # db.session.commit()
    db.session.add(p)

    return "create : "

@app.errorhandler(404)
def page_404(error):

    return render_template("404.html"), 404


@app.errorhandler(500)
def page_500(error):
    return render_template("404.html"), 500

@front.route("token", methods=["POST"])
def get_token():
    """
    Authenticate against dummy data.  Expects POST data: {"username": "username", "password": "password"}
    :return: JSON object {"token": "token"} on successful authentication
    """
    try:
        # body = flask.request.get_json()  # Get JSON POST data
        body = request.form
        username = body.get('username')
        password = body.get('password')

        user = demo.User.query.filter(demo.User.username == username, demo.User.password == password).first()

        if user:  # Authenticate against 'database'
            return create_token(user.id)
        else:
            raise Exception("Invalid credentials")  # Username/password pair did not match what we have
    except Exception as e:
        print(e)
        return "Unauthorized", 401  # Bad authorization


@front.route("token", methods=["UPDATE"])
def update_token():
    """
    Refresh Access Token
    :return: new access token
    """
    try:
        token = request.headers.get("Authorization")  # Token in the format Authorization: Bearer <token>

        decoded = jwt.decode(jwt=token, key=app.secret_key, verify=True, audience="bys", issuer='zxs')
        return create_token(decoded["id"])
    except Exception as e:
        print(e)
        return "验证失败", 401  # Bad authentication

def create_token(user_id):
    # Create JSON claims object
    jwt_claims = {
        "exp": int(time.time()) + (60),  # 过期时间
        "iss": "bysauth",  # 发行人
        "iat": int(time.time()),  # 发布时间.
        "aud": "bys",  # 接收人
        "id": user_id  # Set a custom claim.
    }

    token = jwt.encode(payload=jwt_claims, key=app.secret_key, algorithm="HS512").decode('utf-8')
    jwt_claims['exp'] = jwt_claims['exp'] + 60 * 60 * 24 * 30
    refresh_token = jwt.encode(payload=jwt_claims, key=app.secret_key, algorithm="HS512").decode('utf-8')
    data = {
        'access_token': token,
        'refresh_token': refresh_token
    }
    return jsonify(data)


@apiv1bp.route("/cookie", methods=["GET"])
def get_cookie():
    """
    Example endpoint.
    :return: JSON object with message of "pong", and current Unix timestamp.
    """

    return jsonify(message="请求成功", timestamp=int(time.time()))


@front.route("token", methods=["GET"])
def token():

    return render_template("index2.html")


