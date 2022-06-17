import os

main_path = 'my_project'
dir_path = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(main_path):
    for d in dir_path:
        path = os.path.join(main_path, d)
        os.makedirs(path)
