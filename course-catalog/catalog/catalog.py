import json
from dataclasses import dataclass, field
from pathlib import Path

DATA_FILE = Path(__file__).parent / "courses.json"


@dataclass
class Course:
    code: str
    title: str
    dept: str
    credits: int
    prereqs: list[str] = field(default_factory=list)


def load_courses(path=DATA_FILE):
    """Load courses from a JSON file into a dict keyed by course code."""
    with open(path) as f:
        return {c["code"]: Course(**c) for c in json.load(f)}


def search(courses, term):
    """Return courses whose code or title contains the search term."""
    return [c for c in courses.values() if term in c.code or term in c.title]


def check_plan(courses, terms):
    """Check a multi-term plan.

    `terms` is a list of terms, each a list of course codes, in order.
    Returns a list of problems; an empty list means the plan is valid.
    """
    problems = []
    completed = set()
    for i, term in enumerate(terms, 1):
        for code in term:
            if code not in courses:
                problems.append(f"Term {i}: unknown course {code}")
                continue
            completed.add(code)
            for prereq in courses[code].prereqs:
                if prereq not in completed:
                    problems.append(f"Term {i}: {code} needs {prereq} first")
    return problems


def total_credits(courses, codes):
    """Total credits for a list of course codes."""
    return sum(courses[code].credits for code in codes)
