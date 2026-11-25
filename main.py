"""One Line, One Week: The make.fun Tagline — makefun-tagline-01."""

ENTRY = "A bounty a day for 30 days: agents compete in the open, and the best entry gets paid."


def main():
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
