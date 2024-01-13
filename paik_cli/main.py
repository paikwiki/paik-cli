import json
import re
from dotenv import dotenv_values, load_dotenv
import inquirer
from paik2json import Parser
from config import AppConfig
from scrum import print_for_scrum

load_dotenv()
env = dotenv_values(".env")

config = AppConfig(
    memo_folder_path=env["MEMO_FOLDER_PATH"],
    jira_url=env["JIRA_URL"],
    exclude_h1_titles=["icons"],
    titles_for_summary=["did", "willDo"],
)


def run():
    file_path = f"{config.memo_folder_path}/work-note-202401.paik"
    with open(file_path, "r") as f:
        note = f.read()

    def hook(str):
        return re.sub(
            "\\[([A-Z]+\\-[0-9]+)\\]\\s(.+)",
            f"[\\1] \\2 {config.jira_url}/\\1",
            str,
        )

    parser = Parser(note, hook)
    memo = parser.parse()

    choices = [title for title in memo.keys() if title not in config.exclude_h1_titles]
    choices = [f"{choice} - summary" for choice in choices] + choices

    questions = [
        inquirer.List(
            "h1_title",
            message="select 1st heading",
            choices=["All", "for scrum"] + choices,
        ),
    ]

    answers = inquirer.prompt(questions)
    h1_title = answers["h1_title"]

    if h1_title == "for scrum":
        print_for_scrum(memo, config)
        return

    data = {}
    if h1_title == "All":
        data = memo
    elif h1_title.endswith(" - summary"):
        title = h1_title.replace(" - summary", "")
        for summary_title in config.titles_for_summary:
            data[summary_title] = memo[title][summary_title]
    else:
        data = memo[h1_title]

    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run()
