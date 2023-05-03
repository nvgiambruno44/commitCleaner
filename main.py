from github import Github


def init(org, repo, head, base):
    github = Github()
    repo = github.get_repo(f"{org}/{repo}")
    commits = repo.get_commits()
    recording = False
    changelog = ''
    for commit in commits:
        if commit.sha == head:
            recording = True
        if recording:
            changelog = changelog + "\n" + commit.last_modified + ": " + commit.commit.message
        if commit.sha == base:
            recording = False

    print(changelog)

if __name__ == '__main__':
    init('nvgiambruno44', 'commitCleaner', 'faccbe47cf473d6110474a4e9f00adde32cfe5c7',
         'a5b143051de1f11dcb008f70e03d79a338d1dd99')
