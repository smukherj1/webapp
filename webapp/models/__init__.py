
class ModelTable:
    def __init__(self):
        self.__table = {}
        self.__locked = False
        self.__db = None

    def set_db(self, db):
        self.anl()
        self.__db = db

    def db(self):
        return self.__db

    # Assert not locked
    def anl(self):
        assert(not self.__locked)

    def add(self, name, model):
        self.anl()
        assert(name not in self.__table)
        assert(model is not None)
        self.__table[name] = model

    # Returns None on lookup failure
    def get(self, name):
        return self.__table.get(name, None)

    # Raises KeyError on lookup failure
    def __getattr__(self, attr):
        return self.__table[attr]

    def lock(self):
        self.anl()
        self.__locked = True

    def __str__(self):
        return 'ModelTable (%d models)'%len(self.__table)

model_table = ModelTable()

def __init_db(app):
    from . import db_handle
    db_handle.init(app)

def __init_models(app):
    from . import User

    model_table.add('User', User.User)

    # Now that the db knows about our models
    # make it generate the necessary tables
    from .db_handle import db
    db.create_all()
    model_table.set_db(db)
    model_table.lock()

def init(app):
    __init_db(app)
    __init_models(app)

