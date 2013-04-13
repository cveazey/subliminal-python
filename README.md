Subliminal Python is a project template designed to help get you up and coding quickly with up-to-date Python platforms and practices, while enabling an easy workflow in [Sublime Text 2](http://www.sublimetext.com/2) running on Mac OS X. It encourages a conventional structure for Sublime Text 2 Build Systems to more easily develop, test, and run your Python code with [`virtualenv`](https://pypi.python.org/pypi/virtualenv).

The project skeleton itself is based on [Chapter 46](http://learnpythonthehardway.org/book/ex46.html) of [Zed Shaw's](http://zedshaw.com/) *[Learn Python The Hard Way](http://learnpythonthehardway.org/)*.

To get started, clone this repo and then run the `newproject` script in `./scripts`. It takes two arguments - a package name and a project name. It will rename all the placeholders for you. Make a symlink to your virtual environment's directory at `./subl/virtual_env` (details in [the wiki](https://github.com/cveazey/subliminal-python/wiki/Getting-Started-with-Subliminal-Python-on-Mac-OS-X-Mountain-Lion)). Test that everything worked by opening the Sublime Text project (sometimes you have to immediately close it and re-open it), choosing nosetests from Tools -> Build Systems, and then running the tests with cmd-B. Alternatively, run `nosetests` from Terminal (with your virtualenv activated, natrually) or `python setup.py nosetests`.

Suggested file layout:

* ./scripts/ for utility type helper scripts
* ./docs/ for docs
* ./PACKAGE_NAME/ for your package's source files (`newproject` will rename this for you)
* ./subl/ for Sublime Text 2 project files and scripts to support custom Build Systems. See ./subl/README.md for more information.
* ./tests/ for your tests
