"""
cleaned_inventory_system.py

A secure and PEP8-compliant inventory management script.
Demonstrates use of logging, file handling, and static analysis best practices.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Global stock data (for simple script; consider class for larger apps)
stock_data: Dict[str, int] = {}


def add_item(item: str | None = None,
             qty: int = 0,
             logs: List[str] | None = None) -> None:
    """Add an item with a given quantity to the stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(
            "Invalid input for add_item: item=%s, qty=%s",
            item,
            qty,
        )
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item: str, qty: int) -> None:
    """Remove a quantity of an item from stock safely."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error(
            "remove_item called with invalid types: %s, %s",
            item,
            qty,
        )
        return

    if item not in stock_data:
        logging.warning("Attempt to remove non-existing item: %s", item)
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s", qty, item)
    except (KeyError, ValueError) as exc:
        logging.error("Unexpected error in remove_item: %s", exc)


def get_qty(item: str) -> int:
    """Return quantity of an item (0 if not present)."""
    if not isinstance(item, str):
        logging.error("get_qty called with non-string item: %s", item)
        return 0
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    """Load stock data from a JSON file (if present)."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        stock_data.clear()
        stock_data.update(data)
        logging.info("Loaded stock data from %s", file)
    except FileNotFoundError:
        logging.warning(
            "File not found: %s (starting with empty inventory)",
            file,
        )
    except json.JSONDecodeError:
        logging.error(
            "Invalid JSON in %s; starting with empty inventory",
            file,
        )


def save_data(file: str = "inventory.json") -> None:
    """Save current stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved stock data to %s", file)
    except (OSError, IOError, ValueError) as exc:
        logging.error("Failed to save data to %s: %s", file, exc)


def print_data() -> None:
    """Print current stock in a readable format."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return list of items with quantity below threshold."""
    if not isinstance(threshold, int):
        logging.error(
            "check_low_items called with non-int threshold: %s",
            threshold,
        )
        return []
    return [i for i, q in stock_data.items() if q < threshold]


def main() -> None:
    """Main script execution."""
    add_item("apple", 10)
    add_item("banana", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)  # will warn (not present)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
