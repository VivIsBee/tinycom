# tinycom

A competition about making the smallest self-hosting compiler you can.

## Terminology

Stage 0 compiler - external compiler used to compile stage 1

Stage 1 compiler - the tested code after being compiled by the stage 0 compiler

Stage (n) compiler - the test code compiled by stage (n-1) compiler

## Requirements
- any language allowed
- no obfuscation or minimization techniques can be used (variable/struct names can be shortened as long as there's another version with more descriptive names)
- judged based on character count (with whitespace and comments not counted)
- it must produce an executable for one of the following targets (only one of them is required, you don't have to target more than one):
  - WASM
  - GNU/Linux (ELF executable)
  - Windows (PE executable)
  - MacOS (Mach-O executable)
  - I'll even allow DOS (COM/MZ/PE executable)
- the input must be read either from a file or stdin
- the compiler must not use any standard language facilities that allow executing or compiling code directly (eval in python isn't allowed)
- the compiler cannot produce a static executable that isn't based on the input
- the compiler must be self-hosting and an external compiler must be able to compile it so the code can be tested (the external compiler must either be open source or widely used to ensure the external compiler doesn't just copy its own code or something)
- the stage 2 compiler must be byte-for-byte identical to the stage 3 compiler
