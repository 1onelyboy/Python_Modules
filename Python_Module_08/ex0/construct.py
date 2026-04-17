import sys
import os
import site


def is_virtual_environment():
    return sys.prefix != sys.base_prefix


def main() -> None:
    current_python = sys.executable
    venv_name = os.path.basename(sys.prefix)
    environment_path = sys.prefix
    package_path = site.getsitepackages()[0]
    if is_virtual_environment():
        print(f"""MATRIX STATUS: Welcome to the construct

Current Python: {current_python}
Virtual Environment: {venv_name}
Environment Path: {environment_path}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
{package_path}
{sys.prefix}
{sys.base_prefix}""")
    else:
        print(f"""MATRIX STATUS: You're still plugged in

Current Python: {current_python}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\activate # On Windows

Then run this program again.""")

if __name__=="__main__":
    main()

