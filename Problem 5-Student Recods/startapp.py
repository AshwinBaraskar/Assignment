from flask import Flask, render_template, request
from userinfo import User

app = Flask(__name__)
app.template_folder = 'pages'


@app.route("/user/reg")
def welcome_page():
    print("sample print")
    return render_template('userreg.html')


usersList = []


@app.route("/user/save/", methods=["POST"])
def save_user_info():
    # print(request.form)  # this is the capture the data from post request -->html
    reqdata = request.form
    user = User(reqdata['uid'], reqdata['fnm'], reqdata['lnm'], reqdata['adr'],
                reqdata['gender'])
    usersList.append(user)

    return render_template('userreg.html', msg="User successfully added", users=usersList)


@app.route("/user/delete/<int:userid>", methods=['GET'])
def delete_user(userid):
    print('User Id for Delete: ', userid)

    for user in usersList:
        if user.userId == userid:
            usersList.remove(user)

    return render_template('userreg.html', users=usersList,
                           msg="User removed successfully {}".format(userid))


@app.route("/user/update/<int:userid>", methods=['GET'])
def update_user(userid):
    print('User Id for Update: ', userid)

    for user in usersList:
        if user.userId == userid:
            return render_template('userreg.html', users=usersList, msg="User Updated successfully {}".format(userid))


if __name__ == '__main__':
    app.run(debug=True)
