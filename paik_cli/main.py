import json
import inquirer
from paik2json.line_manager import LineManager
from paik2json.parser import Parser


def run():
    questions = [
        inquirer.Text("file_path", message="File path", default="sample/memo.paik")
    ]
    answers = inquirer.prompt(questions)

    with open(answers["file_path"], "r") as f:
        greeting = f.read()

    parser = Parser(LineManager(greeting))
    print(json.dumps(parser.parse(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run()
