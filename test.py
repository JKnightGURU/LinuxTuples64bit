import linuxtuples
conn = linuxtuples.connect()
conn.put((5.0, 5))
print conn.dump()
conn.put(("123", 1))
print conn.dump()
