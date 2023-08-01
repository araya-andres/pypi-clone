import flask

app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run()


def register_blueprints():
    from views import home_views, package_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)


if __name__ == "__main__":
    main()
else:
    register_blueprints()
