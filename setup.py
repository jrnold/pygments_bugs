from setuptools import setup
entry_points = """
[pygments.lexers]
   stan = pygments_stan:StanLexer
"""

setup(
    name = "pygments_stan",
    version = "0.1",
    py_modules = ['pygments_stan'],
    install_requires = ['pygments >= 1.4'],
    # Metadata
    author = "Jeffrey B. Arnold",
    license = "BSD",
    entry_points = entry_points
)
