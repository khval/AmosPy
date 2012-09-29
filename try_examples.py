"""Try the amos example files with amosToText and see which fail"""
import glob
import os
from amosToText import convert_file, BadTokenRead


def try_conversion(amos_file):
    try:
        lines, unknown_tokens, bytesRead, header = convert_file(amos_file)
        return unknown_tokens
    except BadTokenRead:
        return 1

def main():
    example_root = os.path.expanduser("~/Amiga/disks/AMOSPro_Examples/Examples")
    paths = glob.glob(os.path.join(example_root, "H-*"))
    results = []
    for path in paths:
        amos_files = glob.glob(os.path.join(path, "*.AMOS"))
        _ = [results.append((try_conversion(amos_file), amos_file)) for amos_file in amos_files]
    results = [(result, name) for result, name in results if result != 0]
    print "Unfound tokens or problems found in %d files" % len(results)
    for result, name in results:
        print name


if __name__ == "__main__":
    main()