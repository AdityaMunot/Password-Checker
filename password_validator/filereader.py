def file_reader(path):
    plist = []
    try:
        fp = open(path, 'r', encoding='utf-8')
    except FileNotFoundError:
        raise FloatingPointError(" can't open:", path)

    else:
        with fp:
            for line in fp:
                    fields = line.strip()
                    fields = fields.split()
                    if len(fields) != 1:
                        raise ValueError("Number of fields in the file is not equal to expected number of fields")
                    else:
                        plist.append(fields[0])
    return plist