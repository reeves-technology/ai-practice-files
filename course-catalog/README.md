# Course Catalog (practice repository)

A small, made-up course catalog library and command-line tool. It has a few
deliberate bugs and a missing feature; see `ISSUES.md`. `feature-requests.md`
holds 12 requests from its (fictional) users.

Requires Python 3.10+ and nothing else.

## Getting started

Copy this folder somewhere of your own and make it a git repository, so you
can commit and branch freely:

```
git init && git add . && git commit -m "Initial commit"
```

## Use

```
python -m catalog search biology
python -m catalog show BIO-201
python -m catalog plan BIO-101 CHEM-101 BIO-201
```

## Test

```
python -m unittest
```
