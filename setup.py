from setuptools import setup, find_packages
 
setup (
  name='dafnylexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  dafnylexer = dafnylexer.lexer:DafnyLexer
  """,
)
