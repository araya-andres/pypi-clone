import flask

from infrastructure.view_modifiers import response

blueprint = flask.Blueprint("packages", __name__, template_folder="templates")


@blueprint.route("/project/<package_name>")
def package_details(package_name: str):
    return f"Package details for {package_name}"
