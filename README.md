# Being Creative in Physics

(Note: some of this file was produced by Claude based on earlier material, and then reviewed and revised by F.M. The course description is by F.M.)

*Understanding the thinking behind real research, and learning to use AI efficiently for rapid exploration.*

Interactive seminar by
Florian Marquardt (Friedrich-Alexander-Universität Erlangen-Nürnberg and Max Planck Institute for the Science of Light)

This repository holds the code, notebooks and supporting material for the course.

---

## What this course is about

In this series of interactive lectures, we will learn how to approach open-ended questions in physics, just like in real research, and we will speed up our explorations using AI.

In conventional lectures, you will learn about one topic at a time, and this is reflected in the homework problems, where it is usually known in advance which formulas or physical concepts might be relevant. This is completely unlike real-life research! In the real world, we are facing situations where it is not immediately clear which physical effects are important. In addition, of course we might need to exploit concepts from several different areas of physics at the same time. Even more than that, we initially do not even know which are the right questions to ask!

We want to explore together the thinking that research scientists apply to make progress in such situations. Moreover, we will see how to make the best possible use of AI to help us in the creative process.

We will learn about approaches like order-of-magnitude estimates, constructing simplified toy models, producing hypotheses about how the answer might look like qualitatively, checking for symmetries, dimensional analysis, simple numerical experiments, reasoning by analogy and many more. We will also learn to brainstorm about questions, hypotheses, and potential approximations, as well as to prioritize our ideas and estimate the difficulties involved in various approaches. Finally, we will practice to communicate our tentative results clearly.

## How it works

- You work in **small teams**.
- Each **episode** starts with a physics scenario, sometimes accompanied by a notebook or script from
  this repository. Most episodes take one or two lecture slots.
- Teams brainstorm questions, rank them, explore, and post **signed and time-stamped** intermediate
  results to the course wiki, where the other teams can see them.
- At the end, each team picks one key insight and summarises it in a short write-up.
- The lecturer uses the episodes to discuss general strategies for dealing with the unknown.

The example episode [*Physics on a swing*](episodes/00_physics_on_a_swing) shows
the format for writing up research progress in the wiki. 
## Episodes

| # | Episode | Material |
|---|---------|----------|
| 0 | *Example:* Physics on a swing (shows the wiki format) | [`episodes/00_physics_on_a_swing`](episodes/00_physics_on_a_swing) |
| 1 | The mysterious rule of life | [`episodes/01_mysterious_rule_of_life`](episodes/01_mysterious_rule_of_life) |
| 2 | Galileo's last theorem | *coming soon* |
| 3 | The broken clockwork hypothesis | *coming soon* |
| 4 | Kepler's voyage | *coming soon* |

Further episodes will be added as the course progresses.

## Repository layout

```
README.md          this file
SETUP.md           how to set up Python, VS Code and an AI assistant
requirements.txt   Python packages needed for the course
episodes/          one folder per episode (wiki page, notebooks, scripts, helper files)
toolbox/           (planned) small reusable examples: ODEs, PDEs on a grid, Monte Carlo, plotting, animation, ...
tools/             maintenance scripts for the course material (not needed by students)
```

Some episodes are mysteries, and parts of their helper code are deliberately hidden. Please find out
what the code does by experimenting, not by decoding it, and don't ask your AI assistant to decode it either.

## Getting started

1. Follow [SETUP.md](SETUP.md) to install Python, the required packages, VS Code and an AI assistant.
2. Clone (or download) this repository.
3. Open the folder of the current episode and run its notebook or script.

You can work with **Jupyter notebooks** or with **plain Python scripts**, whichever suits you better.
Notebooks are convenient for interactive exploration and plots. Plain `.py` files are often easier
for AI coding assistants (such as Claude Code or Copilot agent mode) to read, edit and run on their own.

## License

Code is released under the [MIT License](LICENSE); all other content (text, notebooks, figures) under
[CC BY 4.0](LICENSE-CC-BY-4.0.txt). Some episodes have additional authors, named in the episode's README.

