# Setup

(Note: this file was composed by Claude and then reviewed by F.M.)

This guide gets you from zero to running the course notebooks and scripts with an AI assistant.
Please do this **before the first lecture**. The GitHub student verification in particular can take
a few days.

You need:

1. Python 3.10 or newer, with a few scientific packages
2. Visual Studio Code (VS Code), or another editor you like (not necessary when using a tool like claude code in the terminal)
3. Access to an AI coding assistant (at least one per team)
4. A copy of this repository

---

## 1. Python

### Option A: Miniforge (recommended if you have no Python yet)

Miniforge is a minimal, free conda distribution that works on Windows, macOS and Linux.

1. Download the installer from https://github.com/conda-forge/miniforge and run it.
2. Open a new terminal (on Windows: "Miniforge Prompt") and create an environment for the course:

   ```bash
   conda create -n creative python=3.12
   conda activate creative
   pip install -r requirements.txt
   ```

   (Run the last line from inside the repository folder, see step 4 below.)

### Option B: an existing Python installation, with a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Check that it works

```bash
python -c "import numpy, scipy, matplotlib, ipywidgets; print('all good')"
```

## 2. VS Code

Especially if you are using the github copilot setup, you may want to install the free VS Code editor (from Microsoft). For other setups, like claude code in the terminal, no editor is even needed.

1. Install VS Code from https://code.visualstudio.com.
2. Install the extensions **Python** and **Jupyter** (both by Microsoft) from the Extensions panel.
3. Open the repository folder (*File → Open Folder…*).
4. Open a notebook (`.ipynb`). In the upper right corner, click *Select Kernel* and choose the
   environment you created above (`creative` or `.venv`).

To run a plain Python script, open it and click the ▶ button, or run `python script.py` in the
VS Code terminal (*Terminal → New Terminal*).

If you prefer the classic Jupyter interface instead of VS Code, run `jupyter lab` (or
`jupyter notebook`) in the repository folder.

## 3. AI assistant

Each team needs at least one working AI licence. Any capable assistant works. Two options:

### GitHub Copilot (free for students)

1. Create a GitHub account at https://github.com, or use an existing one. Your **university email** must be
   registered with it (you can add it as a secondary address under *Settings → Emails*).
2. Go to *Settings → Billing and licensing → Education benefits* and start an application.
   Choose "student" and your university (e.g. FAU if you are enrolled in Erlangen), share your location, and upload proof of student status (student ID or
   enrollment certificate). You may have to enable two-factor authentication first.
3. Once approved, install the **GitHub Copilot** extension in VS Code and sign in with your GitHub
   account. You can then use Copilot Chat and agent mode directly in your notebooks and scripts.

Verification can take some time, so apply early.

### Claude Code

[Claude Code](https://claude.com/claude-code) is an AI assistant that runs in the terminal or in
VS Code. It can read the files in a folder, write and run code, and look at the results.
It needs a Claude subscription or an API account (this is paid).
Install it following https://docs.claude.com/en/docs/claude-code/overview, then start it with
`claude` from inside the repository folder. F.M.: We extensively use claude code in my research group.

### Tips for using AI in this course

- Describe the **physics** clearly: what the system is, what you want to compute, and what the plot
  should show. Ask for short, readable code.
- **Check** what comes out: dimensions, limiting cases, symmetries, conservation laws, and comparison
  with a back-of-the-envelope estimate. The AI makes mistakes, and catching them is part of the skill.
- Start small (few particles, small grids, short times), then scale up.
- Agent-style assistants work especially well with plain `.py` files that save their plots to disk.

## 4. Get this repository

With git:

```bash
git clone <repository URL>
cd <repository folder>
```

Without git: download the repository as a ZIP file from its GitHub page (*Code → Download ZIP*)
and unpack it.

When new episodes are added, update your copy with `git pull` (or download the ZIP again).

---

## Troubleshooting

- **`ModuleNotFoundError`**: the notebook is using a different Python than the one you installed
  the packages into. Select the right kernel in VS Code, or run `pip install -r requirements.txt`
  in the environment the notebook uses.
- **Interactive widgets (buttons, sliders) do not show up**: make sure `ipywidgets` is installed in
  the kernel's environment, and restart the kernel.
- **Animations are slow**: reduce the grid size or the number of time steps.
