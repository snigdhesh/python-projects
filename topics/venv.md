#### Package Managers
npm and pip

#### Installing libraries
- packages: cowsay, boxen
- Global installation
- local installation

#### venv (virtual environment)
We create virutal environment to configure python properties on local project.
Without this,   
- If you run `app.py`, it's going to pick python interpreter from global scope.
- If you do `pip install pandas`, it's going to install at global scope, instead of local scope.

#### How to create and use a virtual environment?

##### Step 1: Create the virtual environment

    python3 -m venv venv

- Where first `venv` is the module name (built-in Python module)
- Second `venv` is the folder name — you can name it anything

##### Example: `python3 -m venv naga`

---

##### Step 2: Activate the virtual environment

##### Mac / Linux:

    source venv/bin/activate

##### Windows (Command Prompt):

    venv\Scripts\activate.bat

##### Windows (PowerShell):

    venv\Scripts\Activate.ps1

Once activated, your terminal prompt will show `(venv)` at the start.

---

##### Step 3: Install packages (now installs locally)

    pip install pandas

---

##### Step 4: Deactivate when done

    deactivate

---

#### Requirements.txt
- Install all packages from it:
`pip install -r requirements.txt`

- Generate one from your current environment:
`pip freeze > requirements.txt`

- Add a package manually — just add a line like:
`requests==2.31.0`