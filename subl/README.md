To run the project's build systems in a virtual env, do as follows:

1. In Terminal, activate your virtualenv with `source /path/to/virtualenv/bin/activate`.
2. With your virtualenv activated, create a symoblic link inside the `subl` directory with `ln -s $VIRTUAL_ENV /path/to/subl/virtual_env`.

Build systems for the project should conform to these conventions:

1. `cmd` should be set like e.g.: `["/bin/sh", "subl_BUILD_SYSTEM_NAME_HERE.sh"]`
2. `working_dir` should be set to `$project_path` (this will expand to `/path/to/root/folder/subl`).
3. As implied by the conventions above, the build system's real work should be performed with a shell script located in `$project_path`, i.e the `subl` folder in the top level of the project, with the name `subl_BUILD_SYSTEM_NAME_HERE.sh`.
4. The build system script should have as its first line `source subl_common.sh`. `subl_common.sh` activates the virtualenv and changes the working directory to be the root folder of the project (i.e. one folder above `subl`).
