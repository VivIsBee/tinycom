# tinycom

A competition about making the smallest self-hosting compiler you can.

Submissions are accepted between NOW and 06/07/2026 at 00:00 UTC.

To make a submission, copy `submissions/000-template` and fill out the `README.md`, as well as adjusting the `counter.json` file. The program code can be in whatever structure you want, but please don't include large files (>1MB) in it, and all code including dependencies will be counted as part of it. Then, make a PR and rename the folder to `(PR number)-(name without spaces)`.

## Terminology

Stage 0 compiler - external compiler used to compile stage 1

Stage 1 compiler - the tested code after being compiled by the stage 0 compiler

Stage (n) compiler - the test code compiled by stage (n-1) compiler

## Requirements and rules

- any language allowed
- no obfuscation or minimization techniques can be used (variable/struct names and similar can be shortened as long as there's another version with more descriptive names)
- it must produce an executable for one of the following targets (only one of them is required, you don't have to target more than one):
  - WASM
  - GNU/Linux (ELF executable)
  - Windows (PE executable)
  - MacOS (Mach-O executable)
  - DOS (COM/MZ/PE executable)
  - TI-84+CE calculator (8xp executable)
  - Something else if there's an emulator for it available for Linux
- the input program must be read either from a file or stdin
- the compiler must not use any standard language facilities that allow executing or compiling code directly (eval in python isn't allowed)
- the compiler cannot produce a static executable that doesn't change based on the input
- the compiler must produce an output executable to a file, stdout, or stderr
- the compiler must be self-hosting and an external compiler must be able to compile it so the code can be tested (the external compiler must either be open source or widely used to ensure the external compiler doesn't just copy its own code or something)
- the stage 2 compiler must be byte-for-byte identical to the stage 3 compiler
- all code must be 100% written by the submitter without any assistance of any kind from another person (submitting or not) or ANY form of AI. No exceptions, AI is NOT allowed. This also means you cannot like, submit `rustc` to this.
- each submitter can submit multiple submissions, but can only win once overall
- each submission will be considered overall for all categories. you do not have to submit to a specific category
- judging will happen by me, @VivIsBee, going through each submission and deciding which one I meets the criteria for each category best
  - on a related note, I may submit projects BUT they will not be considered for any categories.
- the competition is cancelled if less than 10 people submit at least one submission each
- I may disqualify people at my own discretion for one of, but not limited to, the following reasons:
  - bigotry, including but not limited to racism, sexism/misogyny, homophobia, transphobia, queerphobia, ableism, or more
  - repeatedly submitting projects that do not meet the requirements (legitimately trying and failing is one thing, repeatedly submitting low quality things without legitimately trying to fix issues is a problem)
  - submitting malware
- If a submission goes against the spirit of the competition (i.e. exploiting loopholes in the rules), then I won't allow it. Repeatedly exploiting loopholes will either get you disqualified or get you to help reviewing, depending on how funny it is. tl;dr if you're going to find loopholes in the rules or break them at least be funny about it

## Categories

I'm kinda broke so prizes won't be very good, sorry

- Smallest
  - judged based on character count (with whitespace and comments not counted) using counter.py
  - Prize is $10 amazon gift card to first place winner, $5 amazon gift card to second and third place winner
- Most creative
  - judged based on whichever one I feel like is the overall most creative
  - Prize is $15 amazon gift card
