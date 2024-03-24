from flask import Flask,request ,render_template


obj=Flask(__name__)


@obj.route('/')
def weolcome():
    return "welcome to the Flask"

@obj.route('/cal',methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    numbers1=request.json["numbers1"]
    numbers2=request.json["numbers2"]

    if operation=="add":
       result=numbers1+numbers2

    elif operation=="multiply":
       result=numbers1*numbers2

    elif operation=="division":
       result=numbers1/numbers2

    else:
       result=numbers1-numbers2

    return result




print(__name__)

if __name__=='__main__':
  obj.run()