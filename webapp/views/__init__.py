
def init(app, models):
    import extutils
    extutils.app = app
    extutils.models = models
    import index
