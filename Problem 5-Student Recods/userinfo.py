class User:
    def __init__(self, uid, nm, rl, age, gen):
        self.userId = int(uid)
        self.name = nm
        self.roll_no = rl
        self.age = age
        self.gender = gen

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '''
            User Id : {}
            Name : {}
            Roll Number : {}
            Age : {}
            Gender : {}
        
        '''.format(self.userId, self.name, self.roll_no,
                   self.age, self.gender)