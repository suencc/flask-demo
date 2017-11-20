import flask, jwt
from app import apiv1bp, app, front



@apiv1bp.before_request
def jwt_filter():
    """
    Intercept all requests to validate JSON Web Tokens else return '401 UNAUTHORIZED'.
    :return: Tuple on error else continue to request method
    """
    print(flask.request.path)

    if not flask.request.path == "/token" and not flask.request.path == "/":  # If we aren't requesting a token, enforce authorization
        try:
            token = flask.request.headers.get("Authorization")  # Token in the format Authorization: Bearer <token>
            # token = flask.request.cookies['access_token']
            re = jwt.decode(jwt=token, key=app.secret_key, verify=True, audience="bys", issuer='bysauth')
            print(re)
        except Exception as e:
            print(e)
            return "授权失效", 401  # Bad authentication 401



@apiv1bp.after_request
def after_request(rv):
    # 解决API跨域问题
    rv.headers['Access-Control-Allow-Origin'] = '*'
    return rv
