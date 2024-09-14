from git import Repo
import subprocess



REPO_URL = 'model link'#'https://huggingface.co/ProsusAI/finbert'
CLONE_PATH = 'local path'

# Clone the repository
repo = Repo.clone_from(REPO_URL, CLONE_PATH)

print(f"Repository cloned to {CLONE_PATH}")

# Change directory to the cloned repo
import os
os.chdir(CLONE_PATH)

# Fetch large files if git-lfs is used
subprocess.run(['git', 'lfs', 'install'])
subprocess.run(['git', 'lfs', 'pull'])

print("Large files fetched.")


'''
if getting erro related to lfs
run this commands in terminal
sudo apt-get install git-lfs
git lfs install'''