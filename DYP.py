from itertools import combinations
from msvcrt import getwch
from limited_choice import limited_choice, limited_choice_int

# create a class for tasks to do
class TaskToDo():
    def __init__(self, define_task):
        self.define_task = define_task
        self.points = 0
    
    def add_point(self):
        self.points += 1
    
    def __repr__(self):
        return f'points: {self.points:<2} | {self.define_task}'


# list of things user have to do
things_to_do = []

while True:  
    # collect answers and append to list
    new_task = input('\nwhat do you have to do:\t\t')
    things_to_do.append(TaskToDo(new_task))
    print('A → add new task\t|\tQ → go to determine prio')
    
    # decision
    what_next = limited_choice('A', 'Q')
    if what_next == 'A':
        pass
    elif what_next == 'Q':
        break


# index of things (necessary to create pairs of task classes)
things_to_do_index = [x for x in range(len(things_to_do))]

# pairs of task's indexes (necessary to form questions)
tasks_pairs = combinations(things_to_do_index, 2)


# ask about prio for each pair
def ask_prio():
    for task in tasks_pairs:
        print(f'\nWhat is more important:\n'
              f'1| {things_to_do[task[0]].define_task}\n'
              f'2| {things_to_do[task[1]].define_task}\n\n')
        
        your_prio = limited_choice_int(1, 2)
        if your_prio == 1:
            things_to_do[task[0]].add_point()
        elif your_prio == 2:
            things_to_do[task[1]].add_point()

ask_prio()

print(f'\n>>> YOUR PRIO <<<\n')
for task in sorted(things_to_do, key= lambda x: x.points, reverse=True):
    print(task)