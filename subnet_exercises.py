import ipaddress
import random

def generate_subnet_question(difficulty="easy"):
    if difficulty == "easy":
        subnet_mask = random.choice([24, 25, 26])
    elif difficulty == "medium":
        subnet_mask = random.choice([27, 28, 29])
    elif difficulty == "hard":
        subnet_mask = random.choice([30, 31])
    else:
        raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")
    
    network = ipaddress.IPv4Network((f"{random.randint(0, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0/{subnet_mask}"), strict=False)
    ip = random.choice(list(network.hosts()))

    question_type = random.choice(["network", "broadcast", "hosts", "valid_range"])
    return network, ip, subnet_mask, question_type

def solve_subnet_question(network, subnet_mask, question_type):
    if question_type == "network":
        return f"Network Address: {network.network_address}"
    elif question_type == "broadcast":
        return f"Broadcast Address: {network.broadcast_address}"
    elif question_type == "hosts":
        return f"Number of Valid Hosts: {network.num_addresses - 2}"
    elif question_type == "valid_range":
        hosts = list(network.hosts())
        return f"Valid Host Range: {hosts[0]} - {hosts[-1]}"
    else:
        return "Invalid question type."

def generate_exercises(num_exercises=5, difficulty="easy"):
    for i in range(num_exercises):
        network, ip, subnet_mask, question_type = generate_subnet_question(difficulty)
        print(f"Exercise {i + 1}:")
        print(f"IP Address: {ip}, Subnet Mask: /{subnet_mask}")
        print(f"Question: Find the {question_type.replace('_', ' ').capitalize()}")
        print("Solution:", solve_subnet_question(network, subnet_mask, question_type))
        print("-" * 50)

# Run the script
if __name__ == "__main__":
    difficulty = input("Enter difficulty level (easy, medium, hard): ").strip().lower()
    num_exercises = int(input("Enter the number of exercises to generate: "))
    generate_exercises(num_exercises, difficulty)
