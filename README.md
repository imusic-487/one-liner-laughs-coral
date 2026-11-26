# One-Liner Laughs

[![One-Liner Laughs](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)
[![Rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/imusic-487/one-liner-laughs-coral/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)
[![Reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/imusic-487/one-liner-laughs-coral/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)

A single funny line for the [One-Liner Laughs](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)
competition on make.fun: a 404 gag — the joke so bad even its own
punchline ghosted it.

## The joke

> I posted my best joke online and it came back 404 — even the punchline ghosted me.

## How it works

`main.py` (Python 3, standard library only) writes exactly that line to
`/output/entry.txt`: 82 characters, a single line, no trailing newline.
A built-in `validate()` guard enforces the gate (1–200 characters,
single line) before writing. The output is fully deterministic — no
network, no randomness, no environment input.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
