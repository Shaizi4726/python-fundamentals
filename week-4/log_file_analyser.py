from collections import Counter
import os
import re


def write_logs(file_path, log_data):
    with open(file_path, mode='w', encoding="utf-8") as log_file:
        log_file.writelines(log_data)


def read_and_analyse(file_path):
    errors_count = 0
    warnings_count = 0
    infos_count = 0
    errors = []
    hours_counter = Counter()

    with open(file_path, mode='r', encoding="utf-8") as log_file:
        lines = log_file.readlines()
        pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>(?P<hour>\d{2}):(\d{2}):(\d{2})) (?P<log_level>\w+) (?P<message>.*)"
        for line in lines:
            pattern_match = re.match(pattern, line)

            if not pattern_match:
                continue

            hours_counter[pattern_match['hour']] += 1

            match pattern_match['log_level']:
                case 'ERROR':
                    errors_count += 1
                    errors.append(pattern_match['message'])
                case 'WARNING':
                    warnings_count += 1
                case 'INFO':
                    infos_count += 1

        frequent_hour = hours_counter.most_common(1)[0][0]

    return {"errors_count": errors_count, "warnings_count": warnings_count, "infos_count": infos_count, "error_messages": errors, "frequent_hour": frequent_hour}


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "assets", "server.log")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    log_data = [
        "2026-03-15 02:14:05 INFO Database heartbeat operational\n",
        "2026-03-15 02:14:10 INFO Database heartbeat operational\n",
        "2026-03-15 02:14:15 INFO Database heartbeat operational\n",
        "2026-03-15 02:40:22 ERROR Database connection timeout\n",
        "2026-03-15 02:40:27 ERROR Database connection timeout\n",
        "2026-03-15 05:41:01 WARNING Retrying database connection (Attempt 1/3)\n",
        "2026-03-15 06:23:11 INFO Database heartbeat operational\n",
        "2026-03-15 08:23:15 INFO Database heartbeat operational\n",
        "2026-03-15 08:23:20 ERROR Database connection timeout\n",
        "2026-03-15 11:05:44 WARNING Retrying database connection (Attempt 1/3)\n",
        "2026-03-15 11:05:50 INFO Database heartbeat operational\n",
        "2026-03-15 11:06:12 WARNING Retrying database connection (Attempt 1/3)\n",
        "2026-03-15 13:19:30 ERROR Database connection timeout\n",
        "2026-03-15 14:19:35 INFO Database heartbeat operational\n",
        "2026-03-15 14:19:40 ERROR Database connection timeout\n",
        "2026-03-15 17:51:02 INFO Database heartbeat operational\n",
        "2026-03-15 17:51:08 WARNING Retrying database connection (Attempt 1/3)\n",
        "2026-03-15 19:51:15 INFO Database heartbeat operational\n",
        "2026-03-15 22:04:51 INFO Database heartbeat operational\n",
        "2026-03-15 22:04:55 ERROR Database connection timeout\n",
        "2026-03-15 00:05:00 WARNING Retrying database connection (Attempt 1/3)\n",
    ]

    write_logs(file_path, log_data)

    results = read_and_analyse(file_path)

    print(f"{'=' * 80}")
    print("Log Level Counts")
    print(f"{'=' * 80}\n")

    print(f"Errors Count: {results['errors_count']}")
    print(f"Warnings Count: {results['warnings_count']}")
    print(f"Infos Count: {results['infos_count']}")

    print(f"\n{'=' * 80}")
    print("Error Messages")
    print(f"{'=' * 80}\n")

    for message in results["error_messages"]:
        print(message)

    print(f"\n{'=' * 80}")
    print("Most Frequent Hour")
    print(f"{'=' * 80}\n")

    print(
        f"The most frequent hour of the activity is: {results['frequent_hour']}")


if __name__ == "__main__":
    main()
