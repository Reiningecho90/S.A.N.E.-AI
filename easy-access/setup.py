from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1}},
    data_files=["C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\common_values.csv",
                "C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\data_storing.csv",
                "C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\login.csv",
                "C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\network_storage.csv",
                "C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\secondary_storage.csv",
                "C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\settings.json",
                ],
    windows = [{'script': "S.A.N.E._DEV_VERSION.py"}],
    zipfile = None
)