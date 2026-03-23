import re
import sys
from pathlib import Path


def scan_file(file_path):
    content = Path(file_path).read_text()

    issues = []

    # Detect hardcoded staff IDs (simple pattern)
    if re.search(r'staff_id\s*=\s*["\']\w+["\']', content):
        issues.append("Hardcoded staff_id detected")

    # Detect printing/logging of staff ID
    if re.search(r'print\(.*staff_id.*\)', content):
        issues.append("Printing staff_id is not allowed")

    return issues


def main():
    failed = False

    for file in Path(".").rglob("*.py"):
        issues = scan_file(file)

        if issues:
            failed = True
            print(f"\n❌ Issues in {file}:")
            for issue in issues:
                print(f" - {issue}")

    if failed:
        print("\n🚫 Commit blocked: Staff ID must remain confidential")
        sys.exit(1)
    else:
        print("✅ No confidentiality issues found")


if __name__ == "__main__":
    main()
