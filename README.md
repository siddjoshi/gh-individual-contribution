# GitHub Organization Commit Analysis

This Python script analyzes commits across multiple GitHub organizations, providing insights into commit activity and code changes per user for the previous day in CET timezone.

## Features

- Analyzes commits from multiple GitHub organizations
- Tracks number of commits per user
- Counts lines of code changed per user
- Filters commits for the previous day in CET timezone
- Reads organization list from a configuration file
- Uses GitHub Personal Access Token for authentication

## Prerequisites

- Python 3.x
- GitHub Personal Access Token with appropriate permissions

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file with your GitHub token:
   ```
   GITHUB_TOKEN=your_github_personal_access_token_here
   ```

2. Create an `organizations.txt` file with the GitHub organizations you want to analyze (one per line). Example:
   ```
   github
   microsoft
   azure
   ```

## Usage

Run the script:
```bash
python github_analysis.py
```

The script will analyze commits from the previous day (CET timezone) and display:
- Number of commits per user
- Lines of code changed per user

## Required GitHub Token Permissions

- `repo` (Full control of private repositories)
- `read:org` (Read organization data)

For organizations using SAML SSO, make sure to enable SSO for your token.

## Error Handling

The script includes error handling for:
- Missing GitHub token
- Organization access issues
- Repository access problems
- Commit statistics errors

## Output Example

```
Commit Analysis Results (CET timezone):
==================================================
User: user@example.com
Number of commits: 5
Lines of code changed: 150

User: another@example.com
Number of commits: 3
Lines of code changed: 80
```