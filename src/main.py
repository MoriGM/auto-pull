import tomllib
from git import Repo


def get_repos():
    with open('repos.toml', 'rb') as config:
        data = tomllib.load(config)
        return data
    return []


def main():
    repos = get_repos()

    for config in repos.values():
        repo = Repo(config['path'])
        remote = repo.remote(config['remote'])
        remote.pull()


if __name__ == '__main__':
    main()
