# Open issues

## #1 Bug: Searching "biology" finds nothing

Reported by: advising office

When I search for `biology` I get no results, but searching `Biology` works.
Students don't type capital letters. Search should ignore case.

## #2 Bug: Planner lets students take a course in the same term as its prerequisite

Reported by: registrar

`python -m catalog plan BIO-101 BIO-201` says the plan is valid even when
both courses are in the same term. A prerequisite has to be completed in an
earlier term.

## #3 Feature: Filter search by department

Reported by: department chairs

We'd like `python -m catalog search intro --dept CHEM` to only return
Chemistry courses. Without `--dept`, search should work as it does now.
