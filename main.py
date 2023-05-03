from github import Github


# TODO: token auth, error handling, params
def generateChangeLog(org, repo, head, base):
    recording = False
    changelog = ''
    try:
        for commit in Github().get_repo(f"{org}/{repo}").get_commits():
            if commit.sha == head:
                recording = True
            if recording:
                changelog = changelog + "\n" + commit.last_modified + ": " + commit.commit.message
            if commit.sha == base:
                break

        print(changelog)
    except Exception as e: print(e)


if __name__ == '__main__':
    generateChangeLog('nvgiambruno44', 'commitCleaner', 'faccbe47cf473d6110474a4e9f00adde32cfe5c7',
                      'a5b143051de1f11dcb008f70e03d79a338d1dd99')
