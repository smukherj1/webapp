
def init(app, models):
    # Set up the app and models
    # so that other views can
    # access them
    import views_common as vc
    vc.app = app
    vc.models = models

    # Import all views
    import index
    import register
    import login
