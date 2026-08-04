# ==========================================================
# Configuration
# ==========================================================

BASE_GITHUB_API = "https://api.github.com"

# Number of commits to analyze
MAX_COMMITS = 200

# Optional:
# Add your GitHub Personal Access Token here later
# to increase API rate limits.
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")