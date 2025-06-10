#!/usr/bin/env python3
"""
Script to generate percent usage bars to visually display
a user's quotas
"""

# Built-in package, part of standard library
from math import floor, ceil


def percent_used(usage: float, total: float) -> int:
    """Calculate percentage as nearest int out of 100"""
    return int((usage / total) * 100)


def progress_bar(
    usage: float,
    total: float,
    length: int = 40,
    used_char: str = "#",
    empty_char: str = "-",
) -> str:
    """General mechanism for creating a progress bar"""

    # Round up (so ~zero has one used_char, and within one unit of 100% has all used_char)
    n_used_chars: int = ceil(percent_used(usage, total) * length / 100)
    # Remaining chars must be empty
    n_empty_chars: int = length - n_used_chars

    # Progress bar
    bar: str = f"{used_char * n_used_chars}{empty_char * n_empty_chars}"

    return bar


def formatted_progress_bar(quota_tuple: tuple[float], quant: str) -> str:
    """
    Nicely formatted progress bar.
    Edit this to change any of the formatting.
    """
    usage: float = quota_tuple[0]
    total: float = quota_tuple[1]

    bar: str = progress_bar(usage, total, length=40, used_char="#", empty_char="-")

    return f" {quant}: [{bar}] {usage}/{total} GB {percent_used(usage, total):3.0f}%"


def generate_quota_bars(quota_dict: dict):
    """Generate quota bars for a given quota dict"""
    line_list: list[str] = []
    for dirpath, quantity_dict in quota_dict.items():
        line_list.append(dirpath)
        for quantity, quota_tuple in quantity_dict.items():
            line_list.append(formatted_progress_bar(quota_tuple, quantity))

        line_list.append("")

    # Combine the lines into a single string separated by newlines
    return "\n".join(line_list)


if __name__ == "__main__":
    # Only execute the following if actually running the script.
    # (So the above functions can be imported by a different python script, if desired.)

    # First, get quota_dict

    # TODO: Generate quota_dict using output of new "get_quotas" script
    quota_dict = {
        "/home/ckoch5": {"Size usage": (15, 20)},
        "/staging/ckoch5": {"Size Usage": (10, 100), "Item Usage": (56, 100)},
    }

    # Second, print the quota bars generated from said dict
    print(generate_quota_bars(quota_dict))
