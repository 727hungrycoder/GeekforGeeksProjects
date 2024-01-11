tasks = []

def addTask():
    task = input("Please enter a task")
    tasks.append(task)
    print(f"Tasks {task} added to the list.")    
    
def listTasks():
    if not tasks:
        print("There are no task currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
            
            
def deleteTask():
    listTasks()
    try:
        tasktoDelete = int(input("Enter the task # to delete"))
        if tasktoDelete >=0 and tasktoDelete<len(tasks):
            tasks.pop(tasktoDelete)
            print(f"Task {tasktoDelete} has een removed")
        else:
            print(f"Task {tasktoDelete} was not found")
    except:
        print("Invalid input")
        
            
            

if __name__ == "__main__":
    ## Create a loop to run the app
    print("Welcome to the to do list app")
    
    while True:
        #print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List the tasks")
        print("4. Quit")
        
        
        choice =input("Enter your choice")
        
        
        if choice=="1":
            addTask()
        elif choice=="2":
            deleteTask()        
        elif choice =="3":
            listTasks()
        elif choice =="4":
            break
        else:
            print("Invalid Input")
    print("Good bye")        
        