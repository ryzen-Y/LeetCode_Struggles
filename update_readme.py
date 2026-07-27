import json
import os
import re
import requests

README = "README.md"
LEET_DIR = "leet"

URL = "https://leetcode.com/api/problems/all/"


def get_problems():
    data = requests.get(URL, timeout=30).json()

    problems = {}

    diff_map = {
        1: "Easy",
        2: "Medium",
        3: "Hard"
    }

    for p in data["stat_status_pairs"]:

        num = str(p["stat"]["frontend_question_id"])

        problems[num] = {
            "title": p["stat"]["question__title"],
            "slug": p["stat"]["question__title_slug"],
            "difficulty": diff_map[p["difficulty"]["level"]],
        }

    return problems


leetcode = get_problems()

files = []

for file in os.listdir(LEET_DIR):

    if file.endswith(".py"):

        num = file[:-3]

        if num.isdigit():

            files.append(int(num))

files.sort()

easy = medium = hard = 0

rows = []

for num in files:

    p = leetcode.get(str(num))

    if not p:
        continue

    diff = p["difficulty"]

    if diff == "Easy":
        easy += 1
        emoji = "🟢 Easy"

    elif diff == "Medium":
        medium += 1
        emoji = "🟡 Medium"

    else:
        hard += 1
        emoji = "🔴 Hard"

    rows.append(
        f'| {num} | '
        f'[{p["title"]}](https://leetcode.com/problems/{p["slug"]}/) | '
        f'{emoji} | '
        f'[Python](leet/{num}.py) |'
    )

table = "\n".join(rows)

with open(README, "r", encoding="utf8") as f:
    readme = f.read()

readme = re.sub(
    r'<!-- START_PROBLEMS -->.*?<!-- END_PROBLEMS -->',
    f'<!-- START_PROBLEMS -->\n\n{table}\n\n<!-- END_PROBLEMS -->',
    readme,
    flags=re.S
)

for key, value in {
    "LEET_COUNT": len(files),
    "EASY_COUNT": easy,
    "MEDIUM_COUNT": medium,
    "HARD_COUNT": hard
}.items():

    readme = re.sub(
        rf'<!-- {key} -->.*?<!-- END_{key} -->',
        f'<!-- {key} -->{value}<!-- END_{key} -->',
        readme
    )

with open(README, "w", encoding="utf8") as f:
    f.write(readme)

print("README updated successfully!")
