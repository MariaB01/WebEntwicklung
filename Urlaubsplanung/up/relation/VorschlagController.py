class VorschlagController:

    def __init__(self, app, res):
        self.app = app
        self.res = res
        # self.app.add_route("/vorschlag/{person_id}/{uz_id}", self.res, suffix="vorschlag")
        self.app.add_route("/vorschlaege", self.res, suffix="vorschlaege")
        self.app.add_route("/vorschlag", self.res, suffix="vorschlag")
        self.app.add_route("/vorschlag/{person_id}/{uz_uzid}", self.res, suffix="vorschlag")
        self.app.add_route("/sortiertprio", self.res, suffix="sortiertprio")