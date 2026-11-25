import os

PART_A = "I routed you through a wedding because the map swore the reception was a shortcut. "
PART_B = "You lost 9 minutes, but you did catch the bouquet, so call it even."
LINE = PART_A + PART_B

assert 1 <= len(LINE) <= 200

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
