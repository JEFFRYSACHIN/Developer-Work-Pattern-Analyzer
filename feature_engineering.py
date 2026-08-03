import pandas as pd

# ==========================================================
# Simple Sentiment Analysis
# ==========================================================

POSITIVE_WORDS = {
    "add",
    "added",
    "create",
    "created",
    "improve",
    "improved",
    "success",
    "completed",
    "finish",
    "fixed",
    "update",
    "updated"
}

NEGATIVE_WORDS = {
    "bug",
    "error",
    "failed",
    "failure",
    "remove",
    "removed",
    "issue",
    "crash",
    "broken"
}


def calculate_sentiment(message):

    message = message.lower()

    score = 0

    for word in POSITIVE_WORDS:

        if word in message:
            score += 1

    for word in NEGATIVE_WORDS:

        if word in message:
            score -= 1

    return score

# ==========================================================
# Convert Commit Date to Features
# ==========================================================

def extract_time_features(df):

    df["date"] = pd.to_datetime(df["date"])

    df["commit_hour"] = df["date"].dt.hour

    df["day_of_week"] = df["date"].dt.dayofweek

    df["is_weekend"] = (
        df["day_of_week"] >= 5
    ).astype(int)

    df["is_night"] = (
        (df["commit_hour"] >= 22)
        |
        (df["commit_hour"] <= 5)
    ).astype(int)

    return df


# ==========================================================
# Commit Message Features
# ==========================================================

def extract_message_features(df):

    df["message_length"] = (
        df["message"]
        .fillna("")
        .str.len()
    )

    df["sentiment"] = (
        df["message"]
        .fillna("")
        .apply(calculate_sentiment)
    )

    return df


# ==========================================================
# Feature Engineering Pipeline
# ==========================================================

def engineer_features(df):

    df = extract_time_features(df)

    df = extract_message_features(df)

    return df


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample_data = {

        "repository": [

            "Repo1",

            "Repo1",

            "Repo2"

        ],

        "date": [

            "2026-08-03T23:45:10Z",

            "2026-08-04T09:20:55Z",

            "2026-08-02T00:15:22Z"

        ],

        "message": [

            "Fixed login bug",

            "Updated README",

            "Completed dashboard"

        ]

    }

    df = pd.DataFrame(sample_data)

    df = engineer_features(df)

    print(df)