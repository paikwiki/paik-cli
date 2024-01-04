import json
import re
import inquirer
from paik2json.line_manager import LineManager
from paik2json.parser import Parser
from config import AppConfig

config = AppConfig(memo_folder_path="sample")
JIRA_URL = "https://APP_NAME.atlassian.net/browse"


def run():
    file_path = f"{config.memo_folder_path}/memo-202401.paik"
    with open(file_path, "r") as f:
        greeting = f.read()

    def hook(str):
        return re.sub(
            "\\[([A-Z]+\\-[0-9]+)\\]\\s(.+)",
            f"\\2 {JIRA_URL}/\\1",
            str,
        )

    parser = Parser(LineManager(greeting), hook)
    memo = parser.parse()

    choices = [title for title in memo.keys()]
    questions = [
        inquirer.List(
            "h1_title",
            message="select 1st heading",
            choices=["All"] + choices,
        ),
    ]

    answers = inquirer.prompt(questions)
    h1_title = answers["h1_title"]

    if h1_title == "All":
        data = memo
    else:
        data = memo[h1_title]

    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run()
