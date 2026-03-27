from typing import Iterable, List

DEFAULT_MULTIPLIER = 1.15
DEFAULT_LOG_PATH = "log.txt"


def calculate_total(value: float, multiplier: float = DEFAULT_MULTIPLIER) -> float:
    """Return the scaled total for a single numeric value."""
    return value * multiplier


def format_total(value: float) -> str:
    """Return a human-friendly formatted string for a total."""
    return f"Total: {value:.2f}"


def log_results(results: List[float], path: str = DEFAULT_LOG_PATH) -> None:
    """Append results to a log file. Fails gracefully on I/O errors."""
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(str(results) + "\n")
    except OSError:
        print(f"Warning: could not write to log file {path}")


def process_data(
    data: Iterable[float],
    multiplier: float = DEFAULT_MULTIPLIER,
    log_path: str = DEFAULT_LOG_PATH,
) -> List[float]:
    """Process numeric inputs by scaling, printing formatted totals, and logging.

    Non-numeric items are skipped with a warning. Returns the list of computed totals.
    """
    results: List[float] = []
    for item in data:
        try:
            value = float(item)
        except (TypeError, ValueError):
            print(f"Skipping invalid item: {item!r}")
            continue
        total = calculate_total(value, multiplier)
        print(format_total(total))
        results.append(total)

    if results:
        log_results(results, log_path)

    return results


if __name__ == "__main__":
    # Simple demo / sanity check when run as a script
    sample_data = [10, 20.5, "30", "bad", 0]
    print("Demo: processing sample data ->", sample_data)
    processed = process_data(sample_data)
    print("Processed results:", processed)
