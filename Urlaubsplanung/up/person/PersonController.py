class PersonController:

    def __init__(self, app, res):
        self.app = app
        self.res = res

        self.app.add_route("/persons", self.res, suffix="persons")
        self.app.add_route("/person/{pid}", self.res, suffix="person")
        self.app.add_route("/person", self.res, suffix="person")

