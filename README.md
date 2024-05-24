# Pypi_package_tutorial

Tutorial for how to make pypi package, this is the official basic tutorial, we can get the design philosophy from it. `https://packaging.python.org/en/latest/tutorials/packaging-projects/`

To be short, here is my summerized steps and the appendix steps.

# 1 File arch.

First we need to create a dictionary as the following architecture.

`packaging_name/`\n
`├── LICENSE`
`├── pyproject.toml`
`├── README.md`
`├── src/`
`│   └── packaging_name/`
`│       └── package_data/`
`│           ├── checkpoints.pth`
`│       ├── __init__.py`
`│       └── example.py`
`└── tests/`

The LICENSE, README, init.py and tests will be skipped, it has been described in the official tutorial and are similar to the github repo.

The src is the core codes that should provided by youself, we will put an example as shown below.

The example.py can be several functions/classes, which means you can put several examples here, however, it shouldn't contain any "data" file.

The data file, such as the pretrained deep learning checkpoints, should put into the package-data file.

The pyproject.toml is a kind of head file to describ your project environment, I/O, etc.. the details will be posted later.

# 2 Pyproject.toml

This file is the main part for you to make a pypi package, you need to declare the following points.

* Build system
* Configuration
* Dependency (environment)
* Tools
* Project URL
For build system part[build-system], we select the Hatchling as the backend system in this example.
For Configuration part[project], you need to declare the such items, please not the required-python.
You can specific the dependencies, which is not in this example but you can add it in the `project` part like this
dependencies = [
    "numpy>=1.19.2",
    "scipy>=1.5.2",
    "torch>=1.7.0",
    "opencv-python>=4.5.1.48",
    "Pillow>=8.0.1",
]
The [tool.setuptools] and [tool.setuptools.package-data] is to declare the input files and package data locations.
The [project.urls] is to provide the URLs for users' discussion.

# 3 src 

Organize your functions and python files in the src, the best way is to put them parallelly such as example1.py, exaple2.py, if you need to import the modules from other one, it should be more easy, 
For example, if you want to import module in example1.py from example2.py, you can use `from .example2.py import abc` in example1.py, so that it can find it as your have a init.py file in this path.

# 4 package data
If you want to load data, you need to put your data files in the package_data, and declare it in the pyproject.toml so the package can find it. after that, in the file you need to use the package data, you need to import two modules
`import importlib.resources as pkg_resources`
`from color_enhance_lhuang<your package name> import package_data`
and use the pkg_resources.path to read the file, this example tells you how to load a deep learning model pretrained parameters with torch.  
`with pkg_resources.path(package_data, 'model_best_2842.pth') as model_path:`       
        `checkpoint = torch.load(model_path, map_location=self.device)`

# 5 Generate the package and upload it.
   * Register an account in PyPi in `https://test.pypi.org/account/register/`, you need to generate an API tocken before the following steps.
   * Upgrade your tools `py -m pip install --upgrade build`, `py -m pip install --upgrade twine`
   * Build the package in the package dictionary where the .toml located `py -m build`, it will generate two files (.tar.gz, .whl) in dist 
   * Upload to the website `py -m twine upload --repository testpypi dist/*`

# 6 Install and test your own packages .
Find the website and pip install it as usual.  
BYE-BYE
