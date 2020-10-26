from marshmallow import ValidationError
from flask import request, jsonify
from functools import wraps


def required_params(schema):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    "status": "Bad Request"
                }
                print(dict(error, **{"messages": err.messages}))
                return jsonify(error), 400
            return fn(*args, **kwargs)
        return wrapper
    return decorator
