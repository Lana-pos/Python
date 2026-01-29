"""
A module that implements an achievement tracker for a game.
It analyzes player achievements using set operations.
"""


def achievement_tracker():
    """
    Main function to track and analyze player achievements.
    1. Defines achievement sets for three players.
    2. Computes total unique achievements.
    3. Identifies common achievements among players.
    4. Finds rare achievements held by only one player.
    5. Compares achievements between players.
    6. Displays results of the analysis.
    """
    print("=== Achievement Tracker System ===")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print(f"\nPlayer alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob, charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common}")

    rare = set()
    for i in all_achievements:
        count = 0
        if i in alice:
            count = count + 1
        if i in bob:
            count = count + 1
        if i in charlie:
            count = count + 1
        if count == 1:
            rare.add(i)
    print(f"Rare achievements (1 player): {rare}")
    alice_bob_common = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {alice_bob_common}")

    alice_unique_vs_bob = alice.difference(bob)
    print(f"Alice unique: {alice_unique_vs_bob}")

    bob_unique_vs_alice = bob.difference(alice)
    print(f"Bob unique: {bob_unique_vs_alice}")


if __name__ == "__main__":
    achievement_tracker()
