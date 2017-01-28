
def init(app, models):
    import views_common as vc
    vc.app = app
    vc.models = models
    import index
