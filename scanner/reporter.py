import json
import csv


def save_json(filename, target, open_ports):
    results = {
        "target": target,
        "open_ports": open_ports,
        "total_open": len(open_ports)
    }

    with open(filename, "w", newline="") as file:
        json.dump(results, file, indent=4)

    print(f"Results saved to JSON: {filename}")


def save_csv(filename, target, open_ports):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Target", "Port", "Service"])

        for item in open_ports:
            writer.writerow([
                target,
                item["port"],
                item["service"]
            ])

    print(f"Results saved to CSV: {filename}")