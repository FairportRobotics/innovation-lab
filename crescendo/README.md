# Crescendo

## Prerequisites

Install [Git](https://git-scm.com/downloads), [VS Code](https://code.visualstudio.com/download), and [Python](https://www.python.org/downloads/) onto your computer

## Setup Instructions

### Old School Way
1. Open a Command Prompt

2. Clone the repo

If you have set up an SSH key (preferable)
```console
git clone git@github.com:FairportRobotics/innovation-lab.git
```
else
```console
git clone https://github.com/FairportRobotics/innovation-lab.git
```
Note: See [https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=integrated-terminal](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=integrated-terminal) for instruction on how to clone using VS Code.

3. Change directories into the repo
```console
cd innovation-lab
```

4. Set up a Python Virtual Environment
```console
python -m venv .venv
```

5. Start up VS Code
```console
code
```

6. Add the cloned repo directory to the VS Code workspace and set up the virtual environment to be the default python interpreter.

## Challenges

boss.json is the output from the scouting app developed by Team 578's for crescendo.  Your challenge is to restructure the data to be saved as a single line of a CSV file.
