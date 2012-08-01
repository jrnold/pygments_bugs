from setuptools import setup
entry_points = """
[pygments.lexers]
   bugs = pygments_bugs:BugsLexer
   jags = pygments_bugs:JagsLexer
   stan = pygments_bugs:StanLexer
"""

setup(
    name = "pygments_bugs",
    version = "0.1",
    py_modules = ['pygments_bugs'],
    install_requires = ['pygments >= 1.4'],
    # Metadata
    author = "Jeffrey B. Arnold",
    description = "Pygments lexers for BUGS-like languages",
    license = "BSD",
    entry_points = entry_points
)
