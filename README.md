# Crowd Remover
Remove annoying crowds from a non-stable (taken with a hand camera) movie.


## Source Codes
- detect_objejct_from_movie.py: Extract the background from a stable movie.

```bash
    $ python detect_objejct_from_movie.py [input].mp4 [output]
```

- anti_shake_byECC.py: Stabilize an image with warpMatrix to maximize ECC between two frames.

```bash
    $ python anti_shake_byECC.py [input].mp4 [output]
```

- hconcat.py: concatenate two movies horizontally.

```bash
    $ python hconcat.py [left].mp4 [right].mp4 [output]
```

- utils.py: Utilities for visualize the foreground.

## Result
The result is below:

- Top-left: The original movie
- Bottom-right: Removing crowds without stabilization
- Top-left: The stabilized movie
- Bottom-right: Removing crowds with stabilization

![result](./akamon.gif "result")