from flask import (
    Blueprint,
    render_template,
    redirect,
    request
)

from flask_login import current_user , login_required
from funlab import models

module = Blueprint("courses" , __name__ , url_prefix="/courses")
@module.route("/" , methods = [ "GET" , "POST" ])
def index():
    courses = models.Course.objects()
    return render_template("/courses/index.html" , courses=courses)