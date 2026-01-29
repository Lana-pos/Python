"""
A module that performs analytics on a list of fictional game heroes.
It demonstrates list, dict, and set comprehensions for data analysis.
"""


def ft_analytics_dashboard() -> None:
    """
    Main function to analyze a list of game heroes.
    Demonstrates list, dict, and set comprehensions.
    1. Defines a list of heroes with attributes.
    2. Uses list comprehensions to filter and transform hero data.
    3. Uses dict comprehensions to create mappings of hero attributes.
    4. Uses set comprehensions to find unique attributes.
    5. Combines results to provide overall analytics.
    6. Displays the analytics dashboard.
    """
    heroes = [
        {
            "name": "Harry Potter",
            "score": 2500,
            "house": "Gryffindor",
            "achievements": ["boy_who_lived", "triwizard_champion"],
            "status": "active"
        },
        {
            "name": "Hermione Granger",
            "score": 3000,
            "house": "Gryffindor",
            "achievements": ["polyjuice_master", "prefect"],
            "status": "active"
        },
        {
            "name": "Ron Weasley",
            "score": 1800,
            "house": "Gryffindor",
            "achievements": ["chess_grandmaster"],
            "status": "active"
        },
        {
            "name": "Neville Longbottom",
            "score": 2100,
            "house": "Gryffindor",
            "achievements": ["nagini_slayer"],
            "status": "passive"
        },
        {
            "name": "Luna Lovegood",
            "score": 1500,
            "house": "Ravenclaw",
            "achievements": ["nargle_hunter"],
            "status": "active"
        }
    ]

    print("=== Hogwarts Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    limit = 2000
    high_scorers = [h["name"] for h in heroes if h["score"] > limit]
    print(f"High-level wizards (>{limit}): {high_scorers}")

    boosted = [h["score"] * 2 for h in heroes]
    print(f"Magic levels boosted: {boosted}")

    active = [h["name"] for h in heroes if h["status"] == "active"]
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    scores = {h["name"]: h["score"] for h in heroes}
    print(f"Wizard scores: {scores}")

    counts = {h["name"]: len(h["achievements"]) for h in heroes}
    print(f"Achievement counts: {counts}")

    cats = {
        "Elite": len([h for h in heroes if h["score"] >= 2500]),
        "Standard": len([h for h in heroes if 1800 <= h["score"] < 2500]),
        "Apprentice": len([h for h in heroes if h["score"] < 1800])
    }
    print(f"Wizard categories: {cats}")

    print("\n=== Set Comprehension Examples ===")
    unique_ach = {ach for h in heroes for ach in h["achievements"]}
    print(f"Unique achievements: {sorted(list(unique_ach))}")

    houses = {h["house"] for h in heroes}
    print(f"Participating houses: {houses}")

    print("\n=== Combined Analysis ===")
    total = len(heroes)
    avg = sum(h["score"] for h in heroes) / total
    max_val = max(h["score"] for h in heroes)
    top_name = [h["name"] for h in heroes if h["score"] == max_val][0]

    print(f"Total wizards analyzed: {total}")
    print(f"Total unique achievements: {len(unique_ach)}")
    print(f"Average Magic Level: {avg:.1f}")
    print(f"Top performer: {top_name} ({max_val} points)")


if __name__ == "__main__":
    ft_analytics_dashboard()
