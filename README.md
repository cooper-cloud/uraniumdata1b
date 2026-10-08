# ASX uranium 5B tracker
Static site, no build step. Vercel serves `site/` (see vercel.json).
- Add filings: append rows to `data/5b_clean.csv`, run `python scripts/build_data.py`, commit.
- Prices: GitHub Action `prices` runs weekdays after the ASX close (or run it manually), writing `site/data/prices.json`. Yahoo symbols are `XXX.AX`.
- Deploy: push to GitHub, import the repo in Vercel, no framework, no build command.
