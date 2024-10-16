"""
Настройка окружения
"""

# Установить нужную версию Python;
# Создать виртуальное окружение;
# Работа с зависимостями (pip list, pip freeze, pip install/uninstall);

 project	
1) How to add a library using pip and requirements.txt
- pip install package_name
- pip list 
- py -m pip list
- py -m pip search "query"
- pip freze > requirements.txt 
- pip install -r requirements.txt

constraints.txt ile is used to specify upper or lower bounds for package versions.
- py -m pip install -c constraints.txt
- py -m pip install -c constraints.txt requests numpy
#constraints.txt
    Django>=3.0,<4.0
    requests==2.26.0
    numpy<=1.21.0
#constraints.txt

- python -m pip uninstall some_package
- python -m pip list --outdated - display a list of packages that have a newer version available 

Installing from Wheels
.whl - it's compiled binary file. whl files are a binary distribution format for Python packages
- py -m pip install SomePackage-1.0-py2.py3-none-any.whl
- pip install numpy-1.21.0-cp39-cp39-win_amd64.whl
Installing from Remote Whell Repo 
- py -m pip install https://example.com/package_name-version-py_version.whl
- pip show <package_name>


2) How to install and configure python interpreter
PyCharm
When creating a new project, it will ask for the Python interpreter. 
You can configure it from File > Settings > Project: <project_name> > Python Interpreter

PIP Options: 
Install SomePackage and its dependencies from PyPI using Requirement Specifiers
- py -m pip install SomePackage            # latest version
- py -m pip install "SomePackage==1.0.4"   # specific version
- py -m pip install "SomePackage>=1.0.4"   # minimum version

Install a list of requirements specified in a file. See the Requirements files.
- py -m pip install -r requirements.txt

Upgrade an already installed SomePackage to the latest from PyPI.
- py -m pip install --upgrade SomePackage

Editable installs
'''
Редактируемая установка (или editable install) позволяет вам установить пакет из исходного кода, так что любые изменения, 
которые вы вносите в код, сразу же применяются без необходимости переустановки пакета.
'''
- python -m pip install -e path/to/SomeProject

Install a project from VCS
- py -m pip install "SomeProject@git+https://git.repo/some_pkg.git@1.3.1"
- py -m pip install -e "git+https://git.repo/some_pkg.git#egg=SomePackage" 

Install a particular source archive file.
- py -m pip install "./downloads/SomePackage-1.0.4.tar.gz"

Find pre-release and development versions, in addition to stable versions. By default, pip only finds stable versions.
- py -m pip install --pre SomePackage

Install packages from source.
- py -m pip install SomePackage1 SomePackage2 --no-binary :all:

