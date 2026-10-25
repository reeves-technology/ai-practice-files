import argparse

from .catalog import check_plan, load_courses, search


def main():
    parser = argparse.ArgumentParser(prog="catalog")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="search courses by code or title")
    p_search.add_argument("term")

    p_show = sub.add_parser("show", help="show one course")
    p_show.add_argument("code")

    p_plan = sub.add_parser(
        "plan", help="check a plan; separate terms with '/', e.g. BIO-101 / BIO-201"
    )
    p_plan.add_argument("codes", nargs="+")

    args = parser.parse_args()
    courses = load_courses()

    if args.command == "search":
        for c in search(courses, args.term):
            print(f"{c.code}  {c.title} ({c.credits} cr)")
    elif args.command == "show":
        c = courses.get(args.code)
        if c is None:
            parser.exit(1, f"No course {args.code}\n")
        prereqs = ", ".join(c.prereqs) or "none"
        print(f"{c.code}: {c.title}\nDepartment: {c.dept}\nCredits: {c.credits}\nPrerequisites: {prereqs}")
    elif args.command == "plan":
        terms = [[]]
        for code in args.codes:
            if code == "/":
                terms.append([])
            else:
                terms[-1].append(code)
        problems = check_plan(courses, terms)
        print("\n".join(problems) if problems else "Plan is valid.")


if __name__ == "__main__":
    main()
