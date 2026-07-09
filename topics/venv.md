#### Package Managers
npm and pip

#### Installing libraries
- packages: cowsay, boxen
- Global installation
- local installation

#### venv
We create virutal environment to configure python properties on local project.
Without this,   
- If you run `app.py`, it's going to pick python interpreter from global scope.
- If you do `pip install pandas`, it's going to install at global scope, instead of local scope.

#### How to create virutal environment?
python3 -m venv venv

- Where first `venv` is module name, we are asking python3 to use built-in module called venv
- Second `venv` is the folder name, you can name it anything.       
**Example:** python3 -m venv naga

#### Requirements.txt
- Install all packages from it:
`pip install -r requirements.txt`

- Generate one from your current environment:
`pip freeze > requirements.txt`

- Add a package manually — just add a line like:
`requests==2.31.0`