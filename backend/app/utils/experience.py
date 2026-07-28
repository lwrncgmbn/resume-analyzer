import re

def extract_years(text: str, skill_aliases: list[str]) -> int:
    text = text.lower()

    for alias in skill_aliases:
        # pattern = rf"(\d+)\+?\s*(?:years?|yrs?).{{0,20}}{re.escape(alias)}"
        pattern = rf"(\d+)\+?\s*(?:years?|yrs?).{{0,20}}\b{re.escape(alias)}\b"

        match = re.search(pattern, text)

        if match:
            return int(match.group(1))

    return 0