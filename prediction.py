import pandas as pd

from github_api import (
    get_user,
    get_repositories,
    get_commits
)

from feature_engineering import (
    engineer_features
)

from anomaly_model import (
    train_model,
    predict_anomalies
)


# ==========================================================
# Download All Commits
# ==========================================================

def collect_commit_data(username):

    repositories = get_repositories(username)

    all_commits = []

    for repo in repositories:

        repo_name = repo["name"]

        commits = get_commits(

            username,

            repo_name

        )

        all_commits.extend(commits)

    return repositories, all_commits


# ==========================================================
# Build DataFrame
# ==========================================================

def create_dataframe(commit_data):

    if len(commit_data) == 0:

        raise Exception(
            "No commit data available."
        )

    return pd.DataFrame(commit_data)


# ==========================================================
# Generate Summary
# ==========================================================

def generate_summary(

    user,

    repositories,

    result_df

):

    total_commits = len(result_df)

    anomalies = len(

        result_df[
            result_df["status"] == "Anomaly"
        ]

    )

    normal = total_commits - anomalies

    weekend_activity = round(

        result_df["is_weekend"].mean() * 100,

        2

    )

    night_activity = round(

        result_df["is_night"].mean() * 100,

        2

    )

    average_commit_hour = round(

        result_df["commit_hour"].mean(),

        2

    )

    average_sentiment = round(

        result_df["sentiment"].mean(),

        2

    )

    anomaly_percentage = round(

        (anomalies / total_commits) * 100,

        2

    )

    if anomaly_percentage < 15:

        overall = "Normal Work Pattern"

    elif anomaly_percentage < 30:

        overall = "Moderately Unusual Pattern"

    else:

        overall = "Highly Unusual Pattern"

    return {

        "developer": user["login"],

        "name": user["name"],

        "repositories": len(repositories),

        "followers": user["followers"],

        "total_commits": total_commits,

        "normal_commits": normal,

        "anomalies": anomalies,

        "anomaly_percentage": anomaly_percentage,

        "weekend_activity": weekend_activity,

        "night_activity": night_activity,

        "average_commit_hour": average_commit_hour,

        "average_sentiment": average_sentiment,

        "overall_status": overall

    }


# ==========================================================
# Main Prediction Function
# ==========================================================

def analyze_developer(username):

    print("\nDownloading GitHub Data...")

    user = get_user(username)

    repositories, commit_data = collect_commit_data(

        username

    )

    print(

        f"Collected {len(commit_data)} commits."

    )

    df = create_dataframe(

        commit_data

    )

    df = engineer_features(df)

    model = train_model(df)

    result_df = predict_anomalies(

        model,

        df

    )

    summary = generate_summary(

        user,

        repositories,

        result_df

    )

    return summary, result_df


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    username = input(

        "Enter GitHub Username: "

    )

    summary, result = analyze_developer(

        username

    )

    print("\n")

    print("=" * 60)

    print("Developer Work Pattern Report")

    print("=" * 60)

    for key, value in summary.items():

        print(

            f"{key:25}: {value}"

        )

    print("=" * 60)

    print("\nFirst Five Predictions\n")

    print(

        result[
            [

                "repository",

                "commit_hour",

                "is_weekend",

                "message",

                "status"

            ]

        ].head()

    )