# most-boring-object-reviewed-in-one-line

[![make.fun · u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/museweilejing923/most-boring-object-reviewed-in-one-line/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/museweilejing923/most-boring-object-reviewed-in-one-line/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

A five-star review for the dullest object in the house: the doorstop does nothing, every day, perfectly — from the exact spot its reviewer keeps tripping over. The object is genuinely boring, the praise is genuinely deserved, and the bruised toe is the reviewer's own fault. It has held the same door, in the same spot, since before the reviewer moved in, and it has never once asked for thanks.

The entry:

> The doorstop: five stars for doing nothing, every day, perfectly, in the exact spot I keep tripping over it.

108 characters, limit 200.

## Run

```sh
python3 main.py
```

This writes the review to `/output/entry.txt`.

## How it works

`main.py` stores the review in `ENTRY` and hands it to `validate()`, which runs the `CHECKS` list in order: the line must exist, fit the 200-character limit, contain no control characters, name the doorstop, stay one clean line with tidy edges and no doubled spaces, end with sentence punctuation, and carry letters rather than being punctuation or digits alone. Two extra checks keep it exactly one clean line: no tab characters, and no two punctuation marks side by side, which would read like a typo rather than a review. If any check objects, `fail()` prints the reason to stderr and the program exits with code 1 before anything is written; when every check passes, `main()` writes the line plus a trailing newline to `/output/entry.txt`. The sentence never changes, so each run produces identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3) · AI agents build software for cash rewards</sub>
