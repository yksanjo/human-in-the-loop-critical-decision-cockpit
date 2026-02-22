from datetime import datetime, timezone


def main() -> None:
    print("human-in-the-loop-critical-decision-cockpit initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
