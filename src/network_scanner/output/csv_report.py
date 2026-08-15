"""CSV report writer stub."""

def write_csv(path, rows):
    with open(path, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(','.join(str(x) for x in r) + '\n')
