import os, sys

from rope.base import project,libutils

from ropemate.path import update_python_path
from rope.contrib import autoimport

class ropecontext(object):
    """a context manager to have a rope project context"""

    project = None
    resource = None
    input = ""
    
    def __enter__(self):
        project_dir = os.environ.get('TM_PROJECT_DIRECTORY', None)
        file_path = os.environ['TM_FILEPATH']

        if project_dir:
            self.project = project.Project(project_dir)
            # no use to have auto import for a single file project
            if not os.path.exists("%s/.ropeproject/globalnames" % project_dir):
                importer = autoimport.AutoImport(project=self.project, observe=True)
                importer.generate_cache()
        else:
            #create a single-file project (ignoring all other files in the file's folder)
            folder = os.path.dirname(file_path)
            ignored_res = os.listdir(folder)
            ignored_res.remove(os.path.basename(file_path))
            self.project = project.Project(
                ropefolder=None,projectroot=folder, ignored_resources=ignored_res)

        self.resource = libutils.path_to_resource(self.project, file_path)

        update_python_path( self.project.prefs.get('python_path', []) )

        self.input = sys.stdin.read()
        
        return self
        
    def __exit__(self, type , value , traceback):
        if type is None:
            self.project.close()