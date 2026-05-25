import re

from ...builder.modules.text_task import TextTask
from ...builder.modules.task_exercise import TaskExercise

def parse_to_text_task(text):
    lines = text.splitlines()  
    lines = [s.strip() for s in lines if s.strip()]  

    title = re.sub(r'^#+\s', '', lines[0]) # Topic 
    description = lines[1] #  Task description
    taskExercises = []

    ## Find index of answer markers and split the text accordingly
    matchIndices = [i for i, line in enumerate(lines) if '_Antwortzeilen:_' in line or '_Antwort:_' in line]

    for(_, matchIndex) in enumerate(matchIndices):

        taskdescription = lines[matchIndex - 1] if matchIndex > 0 else '' # Task description
        answerLines = _get_answer_lines(lines[matchIndex]) # Number of answer lines (optional) 
        answerText = _get_answer(lines, matchIndex) # Answer text (optional)

        taskExercises.append(TaskExercise(description=taskdescription, answerLines=answerLines, answerText=answerText ))
    
    return TextTask(title=title, description=description, content=taskExercises)


def _get_answer_lines(line):
    match = re.search(r'_Antwortzeilen:_\s*(\d+)', line)
    if match:
        return int(match.group(1))
    return 0

def _get_answer(lines, matchIndex):
    if '_Antwort:' in lines[matchIndex] and matchIndex + 1 < len(lines):
        return lines[matchIndex +1]
    return None