# ==============================================================================
# Practical No. 1: Vacuum Cleaner Agent
# Q1. VACCUM CLEANER AGENT
# ==============================================================================

table = {
    ('A', 'Dirty'): 'Suck',
    ('A', 'Clean'): 'Right',
    ('B', 'Dirty'): 'Suck',
    ('B', 'Clean'): 'Left'
}

def vaccum_agent(location, Status):
    return table[(location, Status)]

if __name__ == "__main__":
    location = input("Enter location(A/B):")
    Status = input("Enter Status (Dirty/Clean):")
    action = vaccum_agent(location, Status)
    print("Action:", action)
