from distutils.core import setup
import os

CUSTOM_PKG_DIR = os.environ["PY_PKG_DIR"]
DEFAULT_PKG_DIR = "pycriu"

if CUSTOM_PKG_DIR is None or CUSTOM_PKG_DIR == "":
    CUSTOM_PKG_DIR = DEFAULT_PKG_DIR

setup(name = "crit",
      version = "0.0.1",
      description = "CRiu Image Tool (het and UnASL modifications)",
      long_description = """CRiu Image Tool based on the criu-het fork
      which adds a "recode" command for recoding images between ISAs using
      Popcorn embedded data in the original binaries.
      The UnASL modifications do not use these embedded data for this recoding.""",
      author = "CRIU team",
      author_email = "criu@openvz.org",
      url = "https://github.com/xemul/criu",
      package_dir = {CUSTOM_PKG_DIR: 'lib/py'},
      packages = [CUSTOM_PKG_DIR, CUSTOM_PKG_DIR + ".images"],
      package_data={'': ['templates/*.tmpl']},
      scripts = ["crit/crit"]
      )
