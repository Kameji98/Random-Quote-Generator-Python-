#!/usr/bin/env python3
"""
Random Quote Generator

A lightweight CLI app to practice:
- lists/dictionaries
- clean CLI UX
- random selection and filtering
"""

from __future__ import annotations

import random


QUOTES = [
    {"text": "Discipline is choosing what you want most over what you want now.", "author": "Unknown", "tag": "discipline"},
    {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman", "tag": "engineering"},
    {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson", "tag": "programming"},
    {"text": "Small steps every day add up to big results.", "author": "Unknown", "tag": "growth"},
    {"text": "Make it work, make it right, make it fast.", "author": "Kent Beck", "tag": "programming"},
    {"text": "You do not rise to the level of your goals. You fall to the level of your systems.", "author": "James Clear", "tag": "systems"},
    {"text": "Consistency beats intensity.", "author": "Unknown", "tag": "habit"},
    {"text": "Quality is not an act, it is a habit.", "author": "Aristotle", "tag": "quality"},
]


def list_tags() -> list[str]:
    """Return sorted unique tags."""
    return sorted({q["tag"] for q in QUOTES})


def pick_quote(tag: str | None = None) -> dict[str, str]:
    """Pick a random quote, optionally filtered by tag."""
    if tag:
        filtered = [q for q in QUOTES if q["tag"].lower() == tag.lower()]
        if not filtered:
            raise ValueError(f"No quotes found for tag: '{tag}'.")
        return random.choice(filtered)
    return random.choice(QUOTES)


def print_quote(q: dict[str, str]) -> None:
    text = q["text"]
    author = q["author"]
    tag = q["tag"]
    print(f'\n"{text}"')
    print(f"— {author}  [{tag}]\n")


def read_menu_choice() -> str:
    print("Choose an option:")
    print("1) Random quote")
    print("2) Random quote by tag")
    print("3) List available tags")
    print("4) Exit")
    return input("> ").strip()


def main() -> None:
    print("=== Random Quote Generator ===")
    print("A tiny CLI app that prints a random quote.\n")

    while True:
        choice = read_menu_choice()

        if choice == "1":
            print_quote(pick_quote())
        elif choice == "2":
            tag = input("Enter tag (e.g., programming, growth): ").strip()
            try:
                print_quote(pick_quote(tag))
            except ValueError as e:
                print(f"\nError: {e}\n")
        elif choice == "3":
            tags = list_tags()
            print("\nAvailable tags:")
            for t in tags:
                print(f"- {t}")
            print()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select 1–4.\n")


if __name__ == "__main__":
    main()
