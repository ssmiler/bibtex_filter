import bibtexparser
import sys

if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <input bibtex file> <input latex bbl file> <output bibtex file>")

input_bibtex = sys.argv[1]
input_bbl = sys.argv[2]
output_bibtex = sys.argv[3]

# load input bibtex db
with open(input_bibtex) as f:
   input_db = bibtexparser.load(f)

# load output entry ids from .bbl file
with open(input_bbl) as f:
    lines = map(str.strip, f.readlines())
    item_lines = filter(lambda line: line.startswith("\\bibitem{"), lines)
    items = set(map(lambda line: line[9:-1], item_lines))

# filter input db entries
output_db = bibtexparser.bibdatabase.BibDatabase()
input_entries_dict = input_db.entries_dict
input_entries_filtered_dict = filter(lambda kv: kv[0] in items, input_entries_dict.items())
entries = list(map(lambda kv: kv[1], input_entries_filtered_dict))
output_db.entries = entries

# and output them
with open(output_bibtex, 'w') as f:
    bibtexparser.dump(output_db, f)
