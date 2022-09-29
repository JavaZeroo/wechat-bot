from pathlib import Path

def cache_file(filename, content):
    """
    Caches the given file with the given content.
    """
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return path

def read_cache_file(filename):
    """
    Returns the content of the given file.
    """
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.read_text()