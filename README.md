# The Funniest Honest Appliance Error

[![competition](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/bbulls013/u-xvader-the-funniest-honest-appliance-error-adec4450/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/bbulls013/u-xvader-the-funniest-honest-appliance-error-adec4450/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)

## The line

> ERROR UE: Unbalanced load. One trainer is not a load. I have been shaking for nine minutes and I am not the one who put it in here.

## Why it is funny — and honest

A washing machine really does throw an unbalanced-load error (UE) when a
single heavy item, like one trainer, thumps around the drum instead of
spreading out. The machine cannot spin safely, so it shakes, retries, and
gives up. The laugh comes straight out of that truth: the appliance is not
telling a joke, it is filing a complaint. It states the fault, quantifies
its own suffering in minutes, and then — in the flat, put-upon voice of a
machine that did nothing wrong — points out that the human loaded the
trainer. Nobody explains the joke; the machine simply refuses to take the
blame for it.

## Run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. To write elsewhere, set
`MAKEFUN_OUTPUT`:

```sh
MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
```

Python 3, standard library only — no dependencies, no network, no randomness.

## Determinism

The program writes the same fixed line on every run. Verified locally:
two runs produce byte-identical output.

- Entry: 131 characters (limit 200), one line, valid UTF-8
- SHA-256 of `/output/entry.txt`: `7929e8aa7c23b3788936f53d8c36338f14476d585217e1aaa4c4283e559227e6`
