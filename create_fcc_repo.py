from pathlib import Path
import shutil
import subprocess

src = Path(r"c:/Users/YUTHISH KRISHNA H/OneDrive/Documents/GitHub/Git Hub/practice_projects_python/fcc test")
dest = Path(r"c:/Users/YUTHISH KRISHNA H/OneDrive/Documents/GitHub/Git Hub/my free code camp practice projects")

dest.mkdir(parents=True, exist_ok=True)
shutil.copytree(src, dest, dirs_exist_ok=True)

subprocess.run(["git", "init"], cwd=str(dest), check=False)
subprocess.run(["git", "add", "."], cwd=str(dest), check=True)
status = subprocess.run(["git", "status", "--short"], cwd=str(dest), capture_output=True, text=True)
if status.stdout.strip():
    subprocess.run(["git", "commit", "-m", "Add FCC test projects"], cwd=str(dest), check=True)
    print("Created local repo and committed FCC test files.")
else:
    print("Local repo already up to date.")
