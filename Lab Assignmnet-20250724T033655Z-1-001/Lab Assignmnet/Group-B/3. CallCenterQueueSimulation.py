# Call Center Queue Simulation using a Queue (FIFO)

# Define the call queue as a list
call_queue = []

# Add a call to the queue
def addCall(customerID, callTime):
    call = {"CustomerID": customerID, "CallTime": callTime}
    call_queue.append(call)
    print(f"Call from Customer {customerID} added (Call Time: {callTime} mins)")

# Answer the first call in the queue
def answerCall():
    if call_queue:
        call = call_queue.pop(0)
        print(f"Answering call from Customer {call['CustomerID']} (Call Time: {call['CallTime']} mins)")
    else:
        print("No calls to answer.")

# View all calls currently in the queue
def viewQueue():
    if call_queue:
        print("Current Call Queue:")
        for i, call in enumerate(call_queue, 1):
            print(f"{i}. Customer {call['CustomerID']} - {call['CallTime']} mins")
    else:
        print("Call queue is empty.")

# Check if the queue is empty
def isQueueEmpty():
    if not call_queue:
        print("The call queue is empty.")
    else:
        print("The call queue is not empty.")

# Menu to interact with the system
def menu():
    while True:
        print("\n--- CALL CENTER MENU ---")
        print("1. Add Call")
        print("2. Answer Call")
        print("3. View Call Queue")
        print("4. Check if Queue is Empty")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            customerID = input("Enter Customer ID: ")
            callTime = input("Enter Call Time (in minutes): ")
            addCall(customerID, callTime)
        elif choice == '2':
            answerCall()
        elif choice == '3':
            viewQueue()
        elif choice == '4':
            isQueueEmpty()
        elif choice == '5':
            print("Exiting Call Center System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the program
menu()
