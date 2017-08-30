
class User(object):

    def __init__(self):
        self.userInfo = {'admin@gmail.com':{'Fname':'Anto','Sname':'Kip', 'Pwd':'12'}}

    def register(self, Fname, Sname, email, password):
        if email not in self.userInfo.keys():
            self.userInfo[email] = {'Fname': Fname, 'Sname': Sname, 'Pwd': password}
            return "Registration Successful"
        else:
            return "The email is already registered"

    def login(self, email, password):
        if email not in self.userInfo.keys():
            return "Wrong Email"
        elif password!=self.userInfo[email]['Pwd']:
            return "Wrong Password"
        else:
            return "Login Successful"