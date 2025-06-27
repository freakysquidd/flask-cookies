import uuid
import random
import json

from flask import Flask, make_response, request, render_template, redirect, url_for



random_number = [1,2,3,4,5,6,7,8,9,0] 
random_uuid = uuid.uuid4()

ran_uuid = random_uuid
ran_num = random.sample(random_number, 9)
cookie = (f"{ran_uuid}{''.join(map(str, ran_num))}")


app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('index.html')



@app.route('/validate', methods=['POST'])
def validate():
    name = request.form['name']
    password = request.form['password']

    user_found = False

    with open("users.json", "r") as file:
        data = json.load(file)
        for credentials in data:
            if credentials['name'] == name and credentials['password'] == password:
               user_found = True
               break
            
        if user_found:
              response = make_response(redirect('dashboard'))
              cookie = (f"{ran_uuid}{''.join(map(str, ran_num))}")
              response.set_cookie("passport", cookie)
              return response
        else:
            return "invalid username or passowrd", 401

                




@app.route('/dashboard')
def dashboard():
    response = request.cookies.get("passport")

    if not response:
        return "key not found or error in client", 401
    else:
        return response

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("Deleting ur cookies, login again and see u soon, byee")
    response.set_cookie("passport", '', expires=0)
    return response







if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=9999)

