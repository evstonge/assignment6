"""Katttis cold-puter problrm."""

__author__ ="Eli St. Onge"
__date__ = "Oct 10, 2023"

def answer(temps: str) -> int:
    """Finds and returns number of -ve of temps

    Args:
        temps (str): temps separated by space (str)

    Returns:
        int: number of hyphens (-ne temps)
    """
    return temps.count('-')