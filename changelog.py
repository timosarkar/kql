import subprocess
import datetime
import os

def get_new_kql_files_last_week(repo_path='.'):
    since_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    try:
        result = subprocess.run(
            ['git', '-C', repo_path, 'log', '--since=' + since_date, '--pretty=format:%H'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        commit_hashes = result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print("Error fetching git log:", e.stderr)
        return []

    new_kql_files = set()

    for commit in commit_hashes:
        try:
            diff_result = subprocess.run(
                ['git', '-C', repo_path, 'diff-tree', '--no-commit-id', '--name-status', '-r', commit],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            for line in diff_result.stdout.strip().split('\n'):
                if line.startswith('A\t'):
                    filename = line.split('\t')[1]
                    if filename.endswith('.kql'):
                        new_kql_files.add(filename)
        except subprocess.CalledProcessError as e:
            print(f"Error checking commit {commit}:", e.stderr)

    return sorted(new_kql_files)

if __name__ == "__main__":
    repo_directory = '.'
    added_kql_files = get_new_kql_files_last_week(repo_directory)
    if len(added_kql_files) == 0:
        print("No new .kql files added in the last 7 days.")
    else:
        print("🆕 .kql files added in the last 7 days:")
        for f in added_kql_files:
            print(f" - {f}")
