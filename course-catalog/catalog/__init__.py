"""A small course catalog used for AI onboarding exercises."""

from .catalog import Course, load_courses, search, check_plan, total_credits

__all__ = ["Course", "load_courses", "search", "check_plan", "total_credits"]
