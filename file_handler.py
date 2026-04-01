def read_file(file):
    try:
        return file.read().decode("utf-8", errors="ignore")
    except:
        return "Unable to read file."