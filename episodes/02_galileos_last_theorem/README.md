# Episode 2: Galileo's last theorem

> *A mysterious physical system inside a black box. Can you find out what's inside?*

The notebook contains a black box: a function `blackbox(arg0, arg1, arg2)` that returns a measurement
`M` as a function of time `t`. Your task is to find out, by experimenting with the three arguments,
what physical system is hidden inside and what the arguments mean.

Code by Florian Marquardt (2020), MIT License.

## Files

- `wiki_page.md`: the episode description from the wiki (HedgeDoc markdown), with the team
  entries removed.
- `Episode2_BlackBoxChallenge.ipynb`: the notebook, with a small Runge-Kutta solver, an example
  of how to use it, and the black box.
- `Episode2_BlackBoxChallenge.py`: the same as a plain Python file, if you prefer scripts.

## Running it

Open the notebook in VS Code, JupyterLab or Google Colab (see [SETUP.md](../../SETUP.md)) and run the
cells from top to bottom. The cell that defines the black box must be run, but please don't decode
it: finding out what is inside is the point of the episode (and don't let your AI assistant decode
it either).

With the plain Python file, either run `python Episode2_BlackBoxChallenge.py` (runs two examples and
saves the plots as PNG files), or write your own script in the same folder that starts with

```python
from Episode2_BlackBoxChallenge import blackbox
```

## Running an experiment and plotting it

`blackbox(arg0, arg1, arg2)` runs one experiment and returns two arrays: the times `ts` and the
measured values `M` at those times. Optional keyword arguments set the total time `T` (default 300)
and the number of time steps `nsteps` (default 1000).

```python
import matplotlib.pyplot as plt
from Episode2_BlackBoxChallenge import blackbox

ts, M = blackbox(1.0, 0.5, 1.0)        # one experiment
plt.plot(ts, M)
plt.xlabel("t")
plt.ylabel("M")
plt.show()
```

All three arguments can also be NumPy arrays, to run many experiments at once. `M` then has one row
per experiment:

```python
import numpy as np

arg0 = np.linspace(0.5, 2.0, 4)         # four different values of arg0
ts, M = blackbox(arg0, 0.5, 1.0)        # M.shape == (4, len(ts))
for a, m in zip(arg0, M):
    plt.plot(ts, m, label=f"arg0 = {a:.1f}")
plt.xlabel("t")
plt.ylabel("M")
plt.legend()
plt.show()
```

The default time step is fairly coarse. Before you trust a result, check that it stays the same when
you increase `nsteps` (for example `blackbox(1.0, 0.5, 1.0, nsteps=4000)`).
