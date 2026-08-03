import pandas as pd

from sklearn.ensemble import IsolationForest


# ==========================================================
# Features Used by the Model
# ==========================================================

FEATURE_COLUMNS = [

    "commit_hour",

    "day_of_week",

    "is_weekend",

    "is_night",

    "message_length",

    "sentiment"

]


# ==========================================================
# Train Isolation Forest
# ==========================================================

def train_model(df):

    model = IsolationForest(

        n_estimators=100,

        contamination=0.10,

        random_state=42

    )

    model.fit(

        df[FEATURE_COLUMNS]

    )

    return model


# ==========================================================
# Predict Anomalies
# ==========================================================

def predict_anomalies(model, df):

    predictions = model.predict(

        df[FEATURE_COLUMNS]

    )

    scores = model.decision_function(

        df[FEATURE_COLUMNS]

    )

    df = df.copy()

    df["prediction"] = predictions

    df["anomaly_score"] = scores

    df["status"] = df["prediction"].map({

        1: "Normal",

        -1: "Anomaly"

    })

    return df


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample_data = {

        "commit_hour": [

            10,

            11,

            12,

            9,

            10,

            23,

            2,

            11,

            10,

            9

        ],

        "day_of_week": [

            0,

            1,

            2,

            3,

            4,

            5,

            6,

            1,

            2,

            3

        ],

        "is_weekend": [

            0,

            0,

            0,

            0,

            0,

            1,

            1,

            0,

            0,

            0

        ],

        "is_night": [

            0,

            0,

            0,

            0,

            0,

            1,

            1,

            0,

            0,

            0

        ],

        "message_length": [

            14,

            18,

            20,

            16,

            15,

            60,

            55,

            17,

            18,

            15

        ],

        "sentiment": [

            1,

            2,

            1,

            1,

            0,

            -2,

            -3,

            1,

            2,

            0

        ]

    }

    df = pd.DataFrame(

        sample_data

    )

    model = train_model(df)

    result = predict_anomalies(

        model,

        df

    )

    print("\nPrediction Results\n")

    print(

        result[
            [

                "commit_hour",

                "is_weekend",

                "message_length",

                "sentiment",

                "status",

                "anomaly_score"

            ]
        ]

    )   