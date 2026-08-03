from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from prediction import analyze_developer


# ==========================================================
# Flask Configuration
# ==========================================================

app = Flask(__name__)

app.secret_key = "developer_work_pattern_analyzer"


# ==========================================================
# Home Page
# ==========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================================
# About Page
# ==========================================================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ==========================================================
# Analyze Developer
# ==========================================================

@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    username = request.form.get(
        "username"
    )

    if not username:

        flash(
            "Please enter a GitHub username."
        )

        return redirect(
            url_for("home")
        )

    try:

        summary, result_df = analyze_developer(
            username
        )

        anomalies = result_df[
            result_df["status"] == "Anomaly"
        ]

        return render_template(

            "result.html",

            summary=summary,

            anomalies=anomalies.to_dict(
                orient="records"
            )

        )

    except Exception as e:

        flash(str(e))

        return redirect(
            url_for("home")
        )


# ==========================================================
# 404 Page
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404


# ==========================================================
# 500 Page
# ==========================================================

@app.errorhandler(500)
def internal_server_error(error):

    return render_template(
        "500.html"
    ), 500


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    app.run(

        debug=True

    )