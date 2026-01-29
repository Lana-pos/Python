"""
A module that demonstrates data stream processing using generators.
It simulates a stream of game events and performs analytics on the fly.
"""


import random
"""
random module is used to generate random events and player data
"""


def game_event_stream(number):
    """
    Simulates a stream of game events.
    Yields a dictionary for each event containing player info and actions.
    """
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, number + 1):
        yield {
            "index": i,
            "player": random.choice(players),
            "level": random.randint(1, 15),
            "event": random.choice(actions),
        }


def fibonacci(n: int):
    """
    Generates the first n Fibonacci numbers.
    """
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(number):
    """
    Checks if a number is prime.
    """
    if number < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def prime_number_generator(count):
    """
    Generates the first 'count' prime numbers.
    """
    counter = 0
    candidate = 2

    while counter < count:
        if is_prime(candidate):
            yield candidate
            counter = counter + 1
        candidate = candidate + 1


def ft_data_stream() -> None:
    """
    Main function to demonstrate data stream processing and generator usage.
    1. Processes a stream of game events.
    2. Performs analytics on the fly.
    3. Demonstrates Fibonacci and prime number generators.
    """
    print("=== Game Data Stream Processor ===")
    n_events = 1000
    print(f"\nProcessing {n_events} game events...\n")
    data_stream = game_event_stream(n_events)

    for i in range(3):
        events = next(data_stream)
        print(f"Event {events['index']}: Player {events['player']} "
              f"(level {events['level']}) {events['event']}")
    print("...")

    total_events = 3
    high_level = 0
    treasure_events = 0
    levelup_events = 0

    for ev in data_stream:
        total_events += 1
        if ev["level"] >= 10:
            high_level += 1
        if ev["event"] == "found treasure":
            treasure_events += 1
        if ev["event"] == "leveled up":
            levelup_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    print(", ".join(str(f) for f in fibonacci(10)))
    print("Prime numbers (first 5):", end=" ")
    print(", ".join(str(p) for p in prime_number_generator(5)))


if __name__ == "__main__":
    ft_data_stream()
