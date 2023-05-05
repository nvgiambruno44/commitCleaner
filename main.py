from github import Github
import argparse


# TODO: error handling
def generateChangeLog():
    # Handle Args
    parser = argparse.ArgumentParser(description='Changelog comparison util')
    parser.add_argument('-o', '--org', help='The github org', required=True)
    parser.add_argument('-r', '--repo', help='the github repo', required=True)
    parser.add_argument('-n', '--new', help='the most recent', required=True)
    parser.add_argument('-b', '--base', help='the base commit', required=True)
    parser.add_argument('-t', '--token', help='the optional gitlab token', required=False)
    args = vars(parser.parse_args())

    recording = False
    changelog = ''

    try:
        for commit in Github(args['token']).get_repo(f"{args['org']}/{args['repo']}").get_commits():
            if commit.sha == args['new']:
                recording = True
            if recording:
                changelog = changelog + "\n" + commit.last_modified + ": " + commit.commit.message
            if commit.sha == args['base']:
                break

        print(changelog)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    generateChangeLog()
