# ...existing code...
def average_ratios(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    ratios = [100.0 / n for n in numbers if n != 0]
    if not ratios:
        raise ValueError("no non-zero numbers to compute ratios")
    return sum(ratios) / len(ratios)
# ...existing code...