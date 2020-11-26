from src.task import Task

def get_preferred_option(task_1, task_2):
    if (task_1.description or task_2.description == "Clean Dishes") and (task_1.description or task_2.description == "Cook Dinner"):
        return "Clean Dishes"
    elif (task_1.description or task_2.description == "Cook Dinner") and (task_1.description or task_2.description == "Clean Windows"):
        return "Cook Dinner"
    elif (task_1.description or task_2.description == "Clean Windows") and (task_1.description or task_2.description == "Wash Dishes"):
        return "Clean Windows"

