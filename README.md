
# Gantt Chart generator
This is a Python based Gantt Chart generator which reads a collection of grouped tasks and column names from a JSON file and outputs a LaTeX file with the resulting chart.
The Gantt Chart is plotted using the `pgfgantt` LaTeX package.
## How to use
Run this command in bash, modify filenames as necessary.
```
python generate_gantt.py example.json output.tex --chart_title "My Gantt Chart"

```

Then either paste the content of `output.tex` into your favorite LaTeX editor or build it with LaTeX Workshop in VSCode.

## JSON format description
An example JSON file is included in the repo. Feel free to modify this one to suit your needs.
The JSON format is as follows:

```json
{
    "tasks": [
        {
            "name": "Task 1",
            "start": "Time 1",
            "group": 1,
            "duration": 1
        },
        {
            "name": "Task 2",
            "start": "Time 2",
            "group": 2,
            "duration": 1
        }
    ],
    "cols": [
        {
            "name": "Time 1",
            "id": 1
        },
        {
            "name": "Time 2",
            "id": 2
        },
    ],
    "groups": [
        {
            "name": "Group 1",
            "id": 1
        },
        {
            "name": "Group 2",
            "id": 2
        }
    ]
}
```

Each task has a name, a start time, a group id and a duration.
The start time is checked against the names of the columns so it has to match one of those.
Also the column names have to be unique.
The program is not sophisticated enough to check this, so it's your responsibility ;)

## Acknowledgements
Made by Axel Larsson in collaboration with ChatGPT.