# Put your app in here.
from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/<calculation>')
# def do_math(calculation):
#     a = request.args.get('a')
#     b = request.args.get('b')
#     int_a = int(a)
#     int_b = int(b)
#     if calculation == 'add':
#         if isinstance(int_a,int) and isinstance(int_b,int):

#             return str(add(int_a,int_b))
#         else: 
#             return "please enter valid integer argumetns"
        
#     elif calculation == 'sub':
#         if isinstance(int_a,int) and isinstance(int_b,int):

#             return str(sub(int_a,int_b))
#         else: 
#             return "please enter valid integer argumetns"
        
#     elif calculation == 'mult':
#         if isinstance(int_a,int) and isinstance(int_b,int):

#             return str(mult(int_a,int_b))
#         else: 
#             return "please enter valid integer argumetns"
        
#     elif calculation == 'div':
#         if isinstance(int_a,int) and isinstance(int_b,int):

#             return str(div(int_a,int_b))
#         else: 
#             return "please enter valid integer argumetns"
#     else:
#         return "Please enter valid calculation"

#  Further Study

calculations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route('/math/<calc>')
def do_math(calc):
    a = request.args.get('a')
    b = request.args.get('b')
    int_a = int(a)
    int_b = int(b)

    return str(calculations[calc](int_a,int_b))