import subprocess
import datetime
import os
from urllib.parse import quote

def get_repo_info(repo_path='.'):
    try:
        # Get origin URL
        result = subprocess.run(
            ['git', '-C', repo_path, 'remote', 'get-url', 'origin'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        url = result.stdout.strip()
        # Convert SSH URL to HTTPS if needed
        if url.startswith('git@github.com:'):
            url = url.replace('git@github.com:', 'https://github.com/')
        if url.endswith('.git'):
            url = url[:-4]

        # Get current branch
        result_branch = subprocess.run(
            ['git', '-C', repo_path, 'rev-parse', '--abbrev-ref', 'HEAD'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        branch = result_branch.stdout.strip()
        return url, branch
    except subprocess.CalledProcessError as e:
        print("Error getting repo info:", e.stderr)
        return None, None

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
                        folder = os.path.dirname(filename)
                        base_file = os.path.basename(filename)
                        base_file_no_ext = os.path.splitext(base_file)[0]
                        new_kql_files.add((folder, base_file_no_ext, filename))
        except subprocess.CalledProcessError as e:
            print(f"Error checking commit {commit}:", e.stderr)

    return sorted(new_kql_files)

if __name__ == "__main__":
    repo_directory = '.'
    origin_url, branch = get_repo_info(repo_directory)
    added_kql_files = get_new_kql_files_last_week(repo_directory)

    if len(added_kql_files) == 0:
        print("No new KQL queries added in the last 7 days.")
    else:
        print(f"{len(added_kql_files)} New KQL queries added in the last 7 days:")
        for folder, file_no_ext, full_path in added_kql_files:
            if origin_url and branch:
                github_link = f"{origin_url}/blob/{branch}/{quote(full_path)}"  # encode spaces and special chars
            else:
                github_link = "No link available"
            print(f"({folder}) {file_no_ext}\n{github_link}\n")

