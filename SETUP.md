# Setup

(Note: this file was composed by Claude and then reviewed by F.M.)

This guide gets you from zero to running the course notebooks and scripts with an AI assistant.
Please do this **before the first lecture**. The GitHub student verification in particular can take
a few days.

You need:

1. Python 3.10 or newer, with a few scientific packages
2. A way to run notebooks: Visual Studio Code (VS Code), or JupyterLab in your web browser (an editor is not necessary for scripts when using a tool like claude code in the terminal)
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

## 2. Running notebooks and scripts

The episodes come as Jupyter notebooks (`.ipynb`) and plain Python scripts (`.py`). A notebook mixes
text, code cells and their output (plots, animations, interactive widgets). Every notebook runs on a
**kernel**: a Python process in the background that executes the cells. The kernel must belong to the
environment where you installed the packages above. Most notebook problems come from a wrong kernel.

There are two good ways to work with notebooks. Both work fine; pick one.

### Option A: VS Code

Especially if you are using the github copilot setup, you may want to install the free VS Code editor (from Microsoft). For other setups, like claude code in the terminal, no editor is even needed.

1. Install VS Code from https://code.visualstudio.com, or update it if you already have it
   (*Code → Check for Updates…* on macOS, *Help → Check for Updates…* on Windows/Linux).
   Old versions do not show the images embedded in our notebooks.
2. Install the extensions **Python** and **Jupyter** (both by Microsoft) from the Extensions panel.
   After installing or updating extensions, quit VS Code completely and start it again.
3. Open the repository folder (*File → Open Folder…*).
4. Open a notebook (`.ipynb`). In the upper right corner, click *Select Kernel* →
   *Python Environments…* and choose the environment you created above (`creative` or `.venv`).
   If VS Code offers to install `ipykernel` into that environment, accept.
5. Run a cell with Shift+Enter or the ▶ next to it. *Restart* and *Interrupt* are in the toolbar
   at the top of the notebook.

The first time a notebook shows an interactive widget (for example the drawing grid in Episode 1),
VS Code may ask whether it may download supporting files for the widgets from a public package server
(jsDelivr or unpkg). This is normal; allow it. If it suggests installing extra extensions, it is fine
to accept those published by Microsoft.

To run a plain Python script, open it and click the ▶ button, or run `python script.py` in the
VS Code terminal (*Terminal → New Terminal*).

### Option B: JupyterLab in your web browser

JupyterLab is the standard notebook interface. It was installed together with the packages above
(as part of `jupyter`), needs no editor, and runs in your web browser.

1. Open a terminal, activate your environment and go to the repository folder:

   ```bash
   conda activate creative          # or: source .venv/bin/activate
   cd <repository folder>
   jupyter lab
   ```

   This starts a local Jupyter server and opens it in your browser (at an address like
   `http://localhost:8888/lab`). Keep the terminal open while you work. Nothing is sent to the
   internet; the "server" runs on your own computer.
2. Use the file browser on the left to open a notebook, e.g.
   `episodes/01_mysterious_rule_of_life/Episode1.ipynb`.
3. Check the kernel name in the upper right corner of the notebook (normally *Python 3 (ipykernel)*).
   Because you started Jupyter from the activated environment, this kernel uses that environment.
4. Run a cell with Shift+Enter, or run everything with *Run → Run All Cells*. To stop a calculation
   that hangs, press ■ (interrupt) in the toolbar; if that does not help, use
   *Kernel → Restart Kernel…*. Interactive widgets work without any extra installation.
5. Save with Ctrl+S (Cmd+S on macOS). When you are done, choose *File → Shut Down*, or press
   Ctrl+C in the terminal.

`jupyter notebook` instead of `jupyter lab` opens the simpler classic interface, which works the
same way. You can also open a terminal inside JupyterLab (*File → New → Terminal*) to run scripts
with `python script.py`, or to start a terminal-based AI assistant such as Claude Code. If an AI tool
changes a notebook file on disk while it is open, JupyterLab will ask whether to reload it.

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
git clone https://github.com/FlorianMarquardt/Being_Creative_In_Physics.git
cd Being_Creative_In_Physics
```

Without git: download the repository as a ZIP file from its GitHub page (*Code → Download ZIP*)
and unpack it.

When new episodes are added, update your copy with `git pull` (or download the ZIP again).

---

## Troubleshooting

- **`ModuleNotFoundError`**: the notebook is using a different Python than the one you installed
  the packages into. Select the right kernel in VS Code, or run `pip install -r requirements.txt`
  in the environment the notebook uses. In JupyterLab, quit and start `jupyter lab` again from a
  terminal in which your environment is activated.
- **VS Code: cells keep spinning, produce no output and cannot be interrupted**: the kernel never
  started. Usually either (a) VS Code or its extensions were just updated and the old extensions are
  still loaded: quit VS Code completely and start it again; or (b) the selected kernel is a Python
  without `ipykernel` (e.g. a system Python): choose your course environment via *Select Kernel*.
- **VS Code: images inside a notebook show as broken**: update VS Code (see Option A above).
- **`jupyter: command not found`**: your environment is not activated in this terminal
  (`conda activate creative` or `source .venv/bin/activate`).
- **Interactive widgets (buttons, sliders) do not show up**: make sure `ipywidgets` is installed in
  the kernel's environment, and restart the kernel. In VS Code, allow the download of the widget
  support files when asked (see Option A above).
- **Animations are slow**: reduce the grid size or the number of time steps.
