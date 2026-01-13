import random
from collections import Counter  # For counting sampled outcomes

# Jelly types and their probabilities (toy likelihood model)
jelly_types = {
    ("red", "sweet"): 0.25,
    ("red", "sour"): 0.25,
    ("yellow", "sweet"): 0.25,
    ("yellow", "sour"): 0.25
}

# Monte Carlo simulation of jelly draws
def simulate_jelly_draws(n):
    # List of jelly combinations and their corresponding probabilities
    combinations = list(jelly_types.keys())
    probabilities = list(jelly_types.values())
    
    # Random sampling according to the true probability distribution
    results = random.choices(combinations, weights=probabilities, k=n)

    # Count empirical frequencies
    counts = Counter(results)

    # Print results
    print(f"\nResults after {n} draws:")
    for combo in combinations:
        color, taste = combo
        count = counts[combo]
        print(f"{color.capitalize()} & {taste.capitalize()}: {count}")
        
if __name__ == "__main__":
    while True:
        try:
            n = int(input("\nEnter the number of jelly draws (0 to exit): "))
            if n == 0:
                print("Exiting the program.")
                break
            elif n > 0:
                simulate_jelly_draws(n)
            else:
                print("Please enter a non-negative integer.\n")
        except ValueError:
            print("Please enter a valid integer.\n")
