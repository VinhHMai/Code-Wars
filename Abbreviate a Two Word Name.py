def abbrev_name(name):
    splitname = name.split()
    print(name)
    return (splitname[0][0].upper() + "." + splitname[1][0].upper())

print(abbrev_name("sam harris")) # S.H