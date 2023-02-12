time_taken = float(input("Enter the time taken by the worker (in hours): "))

if time_taken >= 2 and time_taken < 3:
    print("The worker is highly efficient.")
elif time_taken >= 3 and time_taken < 4:
    print("The worker is ordered to improve speed.")
elif time_taken >= 4 and time_taken < 5:
    print("The worker is given training to improve speed.")
else:
    print("The worker has to leave the company.")
