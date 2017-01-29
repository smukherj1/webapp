
def init(app, models):
    # Set up the app and models
    # so that other views can
    # access them
    from . import views_common as vc
    vc.app = app
    vc.models = models

    # Import all views
    from . import index
    from . import register
    from . import login
