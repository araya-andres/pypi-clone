import flask

from infrastructure.view_modifiers import response
from services.package_service import get_latest_packages

blueprint = flask.Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    return {"packages": get_latest_packages()}


@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    return {}
