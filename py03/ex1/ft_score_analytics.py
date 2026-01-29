"""
A module that performs analytics on player scores provided via
command-line arguments.
It calculates total players, sum, average, high, low, and range of scores.
"""


import sys
"""
sys module is used to handle command-line arguments
"""


def score_analytics():
    """
    Main function to analyze player scores from command-line arguments.
    1. Parses scores from arguments.
    2. Computes total players, sum, average, high, low, and range.
    3. Displays the results.
     4. Handles invalid inputs gracefully.
    """
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(f"No scores provided. Usage: {sys.argv[0]} <score1>"
              "<score2> ...")
        return

    scores = []
    for a in sys.argv[1:]:
        try:
            score = int(a)
            scores.append(score)
        except ValueError:
            print(f"Skipping invalid input: '{a}'")

    if scores:
        total_players = len(scores)
        total_sum = sum(scores)
        max_score = max(scores)
        min_score = min(scores)
        avg_score = total_sum / total_players
        score_range = max_score - min_score

        print(f"Scores processed: {scores}")
        print(f"Total Players: {len(scores)}")
        print(f"Total score: {total_sum}")
        print(f"Average score: {avg_score}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {score_range}")
    else:
        print("No valid numeric scores were found.")
        return


if __name__ == "__main__":
    score_analytics()
