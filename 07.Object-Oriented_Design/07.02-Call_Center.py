'''
07.02 Call Center: Imagine you have a call center with three levels of employees: respondent, manager,
    and director. An incoming telephone call must be first allocated to a respondent who is free. If the
    respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
    free or not able to handle it, then the call should be escalated to a director. Design the classes and
    data structures for this problem. Implement a method dispatchCall() which assigns a call to
    the first available employee.
'''

class Employee:
    def __init__(self, number, level, status):
        self.number = number
        self.level = level
        self.status = status

class Call:
    def __init__(self, caller, hardLevel):
        self.caller = caller
        self.hardLevel = hardLevel

def create_staff():
    # 0-9 are respondents; 10-19 are managers; 20-29 are directors;
    respondents = [Employee(i, i, True) for i in range(30) if i < 10]
    managers = [Employee(i, i, True) for i in range(30) if 10 <= i < 20]
    directors = [Employee(i, i, True) for i in range(30) if i >= 20]
    return respondents, managers, directors

def handle_call(c, respondents, managers, directors, stack):
    str_ = ""
    # First, find an available respondent
    for e in respondents:
        if e.status:
            stack.append(e)
            e.status = False
            break

    if c.hardLevel < 10:
        return str_ + f"Respondent {stack[-1].number} handled the call"

    # If the difficulty is greater, forward it to a manager
    elif 10 <= c.hardLevel < 20:
        for e in managers:
            if e.status:
                stack.pop().status = True
                stack.append(e)
                e.status = False
                return str_ + f"Manager {stack[-1].number} handled the call"

    # If the difficulty is even greater, forward it to a director
    for e in directors:
        if e.status:
            stack.pop().status = True
            stack.append(e)
            e.status = False
            return str_ + f"Director {stack[-1].number} handled the call"

    return str_ + "System is busy, please wait"
