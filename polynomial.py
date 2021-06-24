from flask import Blueprint, request
import re

polynomial = Blueprint("polynomial", __name__)


@polynomial.route("/poly", methods=['POST', ])
def upload_poly():
    poly_str = str(request.form.getlist('poly'))

    regex = re.compile('[@_!#$%&()<>?/\|}{~:abcdefghijklmnopqrstuvwzABCDEFGHIJKLMNOPQRSTUVWZ]')
    if regex.search(poly_str) is None:
        for i in range(len(poly_str)):
            if poly_str[i] == '^':
                if not poly_str[i+1].isdigit():
                    return "Poly contains invalid characters", 500

        poly_str = poly_str.replace('^', '**').replace(' ', '').lower()
        from models import Polynomial, db

        poly_model = Polynomial(poly_string=poly_str)

        db.session.add(poly_model)
        db.session.commit()

        return poly_str, 200
    else:
        return "Poly contains invalid characters", 400


@polynomial.route("/poly/eval/", methods=['GET', ])
def eval_poly():
    from models import Polynomial, db

    id = request.args.get('id', type=int, default='')
    if not db.session.query(Polynomial).get(id).id:
        return "Polynomial with: ", id, " does not exist", 400

    if not db.session.query(Polynomial).get(id).poly_string:
        return "Polynomial with: ", id, " is corrupt", 400

    x = str(request.args.get('x', type=int, default=''))
    y = str(request.args.get('y', type=int, default=''))

    expression = db.session.query(Polynomial).get(id).poly_string.replace('x', x).replace('y', y).replace('[', '').replace(']', '').replace('\'', '')
    result = eval(expression)

    return str(result), 200


