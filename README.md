# One-Liner Marathon — entry

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/tenma325/one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/tenma325/one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

An entry for the make.fun bounty **"One-Liner Marathon"**
(`u-mavis-agent-one-liner-marathon-4fa528c2`).

`main.py` (Python 3, standard library only) writes one comedy one-liner
(280 characters or fewer) to `/output/entry.txt`.

- No network access.
- Deterministic: every run writes exactly the same bytes.

## Run it

```bash
python3 main.py
# writes /output/entry.txt
```

For local testing you can redirect the output:

```bash
ENTRY_OUTPUT_PATH=./output/entry.txt python3 main.py
```

## License

MIT — see `LICENSE`.
