import json
import argparse

# Load tasks, columns and groups from a JSON file
def get_gantt_data(filename):
    # open the file
    with open(filename) as f:
        data = json.load(f)

    # access the data
    tasks = data['tasks']
    cols = data['cols']
    groups = data['groups']

    return tasks, cols, groups

# For each group, associate the group with tasks
def get_group_tasks_ids(groups, tasks):
    # loop over groups
    for group in groups:
        g_id = group["id"]
        task_id_list = [i for i,task in enumerate(tasks) if task["group"] == g_id]
        group["task_ids"] = task_id_list
    return

# Generate a LaTeX document from the loaded tasks, columns and groups
def generate_gantt_chart(tasks, cols, groups, title):

    # Get ids of tasks
    col_names = [col['name'] for col in cols]
    col_ids = [col['id'] for col in cols]
    task_ids = [col_ids[col_names.index(task['start'])] for task in tasks]
    
    # Initialize document
    chart_template = "\\documentclass[tikz]{standalone} \n \\usepackage{pgfgantt} \n \\begin{document} \n"
    chart_template += "\\begin{ganttchart}"
    chart_template += "[hgrid, vgrid,canvas/.append style={{fill=none, draw=black, line width=0.75pt}}, x unit = 2.5cm,y unit title = 1.0cm,y unit chart = 1.0cm,bar/.append style={{draw=none, fill=black}}]"
    chart_template += "{{1}}{{{}}}\n".format(len(cols))
    chart_template += "  \\gantttitle{{{}}}{{{}}}\n".format(title, len(cols))
    chart_template += "  \\\\\n"

    # Add columns
    for col in cols:
        chart_template += "  \\gantttitle{{{}}}{{1}}{{{}}}\n".format(col['name'], col['id'])

    # Add groups
    for group in groups:
        chart_template += "  \\\\\n"
        chart_template += "\\ganttgroup[/pgfgantt/group/.style={{}},inline=false]{{{}}}{{2}}{{1}}".format(group["name"])
        # Add tasks
        for id in group["task_ids"]:
            task = tasks[id]
            chart_template += "  \\\\\n"
            chart_template += "  \\ganttbar{{{}}}{{{}}}{{{}}}\n".format(task['name'], task_ids[id], task_ids[id] + task['duration']-1)

    chart_template += "\\end{ganttchart}\n"
    chart_template += "\\end{document}\n"
    
    return chart_template


def main(args):
    # Main script
    tasks, cols, groups = get_gantt_data(args.json_file)
    chart_title = args.chart_title
    get_group_tasks_ids(groups, tasks)
    gantt_chart = generate_gantt_chart(tasks, cols, groups, chart_title)
    # Write to file
    with open(args.output_file, 'w') as f:
        f.write(gantt_chart)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Gantt chart from JSON file')
    parser.add_argument('json_file', type=str, help='path to JSON file containing tasks data')
    parser.add_argument('output_file', type=str, help='path to output file')
    parser.add_argument('--chart_title', type=str, default='Timeline', help='title for Gantt chart')
    args = parser.parse_args()
    main(args)
