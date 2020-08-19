from weppy import App
from weppy.dal import Field, Model

from weppy import DAL
from weppy.tools import service

app = App(__name__)
app.config.db.uri = 'sqlite://corals.db'

class Coral(Model):
    file = Field('text')
    species = Field('text')
    date = Field('text')
    score = Field('float')
    rank = Field('int')



db = DAL(app, auto_migrate=False)
app.common_handlers = [
    db.handler,
]

db.define_models(Coral)

rows = Coral.all().select()


@app.route("/")
def corals():
    return None

@app.route("/corals")
@service.json
def coraldata():
    return dict(data=rows)

if __name__ == "__main__":
    app.run()