# ==============================================================================
# Practical No: 1(B)
# Question: Table driven Agent for an Autonomous Taxi
# Percept_Action table
# ==============================================================================

table = {
    ('Red', 'Obstacle'): 'Stop',
    ('Green', 'Clear'): 'Move Forward',
    ('Yellow', 'Clear'): 'Slow Down',
    ('Speed limit exceeded', 'Moving'): 'Reduce Speed',
    ('Passenger', 'Waiting'): 'Pick up',
    ('Obstacle', 'Moving'): 'Apply Brake',
    ('Destination', 'Reached'): 'Drop Passenger'
}

def taxi_agent(signal, situation):
    return table.get((signal, situation), "No Action")

if __name__ == "__main__":
    signal = input("Enter signal(Red/Yellow/Speed limit exceeded/Passenger/Obstacle/Destination): ")
    situation = input("Enter Situation(Obstacle,Clear,Clear,Moving,Waiting,Moving,Reached): ")
    action = taxi_agent(signal, situation)
    print("Action:", action)
