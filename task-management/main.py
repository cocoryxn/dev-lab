class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def read_task(self):
        return {
            "Title": self.title,
            "Description": self.description,
            "Status": self.status
        }

    def update_status(self, updated_status):
        self.status = updated_status


class Lead:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)


class Member:
    def __init__(self):
        self.tasks = []

    def receive_task(self, task):
        self.tasks.append(task)


# Create objects
lead = Lead()
member = Member()

# Create one task
task1 = Task(
    "Build AI System",
    "Develop an AI-powered task management system.",
    "In Progress"
)

# Share the SAME task object
lead.create_task(task1)
member.receive_task(task1)

# Read task
print(lead.tasks[0].read_task())
print(member.tasks[0].read_task())

# Member updates the task
member.tasks[0].update_status("Completed")

# Lead can see the updated status
print(lead.tasks[0].read_task())