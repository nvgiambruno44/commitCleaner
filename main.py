from github import Github


def init(org, repo, head, base):
    github = Github()
    repo = github.get_repo(f"{org}/{repo}")
    commits = repo.get_commits()
    recording = False
    changelog = ''
    for commit in commits:
        if commit.sha == base:
            recording = True
        if recording:
            changelog = changelog + "\n" + commit.last_modified + ": " + commit.commit.message
        if commit.sha == head:
            recording = False

    print(changelog)


if __name__ == '__main__':
    init('nvgiambruno44', 'commitCleaner', '65aa95a5ae0ecea6e1b79fb230ff171ef31d7158', '16b6e9ac270b341cbde0cbf2096536ca7ffb6411')
