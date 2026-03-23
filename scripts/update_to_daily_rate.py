from pathlib import Path

FILE_PATH = Path("wage_calculator.py")


def transform_code(content: str) -> str:
    # Replace variable names safely
    content = content.replace("hours_worked", "days_worked")
    content = content.replace("hourly_rate", "daily_rate")

    # Replace input prompt text
    content = content.replace("hours worked", "days worked")

    # Replace hourly rate value (only the specific assignment line)
    lines = content.splitlines()
    updated_lines = []

    for line in lines:
        if "hourly_rate = 10" in line:
            updated_lines.append(line.replace("10", "80"))
        else:
            updated_lines.append(line)

    return "\n".join(updated_lines)


def main():
    original = FILE_PATH.read_text()
    updated = transform_code(original)

    FILE_PATH.write_text(updated)
    print("Refactor complete: hourly → daily rate")


if __name__ == "__main__":
    main()
