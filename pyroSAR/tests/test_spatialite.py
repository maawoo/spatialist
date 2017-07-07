
try:
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    import sqlite3

print(sqlite3.__file__)

con = sqlite3.connect(':memory:')

con.enable_load_extension(True)

con.execute('SELECT load_extension("libspatialite")')
