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
        if commit.sha == head:
            recording = False
        if recording:
            changelog = changelog + "\n" + commit.last_modified + ": " + commit.commit.message

    print(changelog)


if __name__ == '__main__':
    init('octocat', 'Hello-World', '7fd1a60b01f91b314f59955a4e4d4e80d8edf11d',
         '762941318ee16e59dabbacb1b4049eec22f0d303')
