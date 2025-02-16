import os
from datetime import datetime, timedelta
from collections import defaultdict
import pytz
from github import Github
from dotenv import load_dotenv

def get_organizations():
    with open('organizations.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_yesterday_range():
    cet = pytz.timezone('CET')
    now = datetime.now(cet)
    yesterday = now - timedelta(days=1)
    start_date = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
    return start_date, end_date

def analyze_commits():
    load_dotenv()
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable is not set")

    g = Github(github_token)
    organizations = get_organizations()
    start_date, end_date = get_yesterday_range()
    
    commit_counts = defaultdict(int)
    line_counts = defaultdict(int)
    
    for org_name in organizations:
        try:
            org = g.get_organization(org_name)
            repos = org.get_repos()
            
            for repo in repos:
                try:
                    commits = repo.get_commits(since=start_date, until=end_date)
                    for commit in commits:
                        author_email = commit.commit.author.email
                        commit_counts[author_email] += 1
                        
                        # Count lines changed
                        try:
                            stats = commit.stats
                            total_changes = stats.additions + stats.deletions
                            line_counts[author_email] += total_changes
                        except Exception as e:
                            print(f"Error getting stats for commit {commit.sha} in {repo.name}: {e}")
                            
                except Exception as e:
                    print(f"Error processing repository {repo.name}: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error processing organization {org_name}: {e}")
            continue
    
    return commit_counts, line_counts

def main():
    try:
        commit_counts, line_counts = analyze_commits()
        
        print("\nCommit Analysis Results (CET timezone):")
        print("=" * 50)
        for author, count in sorted(commit_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"\nUser: {author}")
            print(f"Number of commits: {commit_counts[author]}")
            print(f"Lines of code changed: {line_counts[author]}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()