from bz2 import compress
import camelot
tables = camelot.read_pdf('', pages='1')
print tables

tables.export('', compress=True)
tables[0].to_csv('')