#! /usr/bin/env python3
import argparse, os, sys

if sys.version_info <= (3, 0):
    print("python 3.x required")
    exit(1)

def preview(run_for_files, run_for_folders, path, desired_depth, lowercase, uppercase, replacements):
    print('\n#### preview ####\n')
    for root, dirnames, files in os.walk(path, topdown=True):
        current_depth = root.count(os.sep) - path.count(os.sep)
        if current_depth > desired_depth:
            break

        if run_for_folders:
            for dirname in dirnames:
                    new = dirname
                    if lowercase:
                        new = dirname.lower()
                    elif uppercase:
                        new = dirname.upper()
                    for r in replacements:
                        new = new.replace(r[0], r[1])
                    print(os.path.join(root, dirname), '>>', new)

        if run_for_files:
            for file in files:
                # remove file extension before manipulation
                new, ext = os.path.splitext(file)[0], os.path.splitext(file)[1]
                if lowercase:
                    new = new.lower()
                elif uppercase:
                    new = new.upper()
                for r in replacements:
                    new = new.replace(r[0], r[1])
                    new += ext
                print(os.path.join(root, file), '>>', new)

    if not run_for_files and not run_for_folders:
        print("nothing to preview, please select --files, --folders or both")
        exit(1)

def execute_change(run_for_files, run_for_folders, path, desired_depth, lowercase, uppercase, replacements):
    errors = 0
    for root, dirnames, files in os.walk(path, topdown=False):
        current_depth = root.count(os.sep) - path.count(os.sep)
        if not current_depth > desired_depth:
            if run_for_folders:
                for dirname in dirnames:
                    new = dirname
                    if lowercase:
                        new = dirname.lower()
                    elif uppercase:
                        new = dirname.upper()
                    for r in replacements:
                        new = new.replace(r[0], r[1])
                    print(os.path.join(root, dirname), '>>', new)
                    try:
                        os.rename(os.path.join(root, dirname), root + '\\' + new)
                    except PermissionError as p:
                        print('Permission denied,', p)
                        errors += 1

            if run_for_files:
                for file in files:
                    # remove file extension before manipulation
                    new, ext = os.path.splitext(file)[0], os.path.splitext(file)[1]
                    if lowercase:
                        new = new.lower()
                    elif uppercase:
                        new = new.upper()
                    for r in replacements:
                        new = new.replace(r[0], r[1])
                        new += ext
                    print(os.path.join(root, file), '>>', new)
                    try:
                        os.rename(os.path.join(root, file), root + '\\' + new)
                    except PermissionError as p:
                        print('Permission denied,', p)
                        errors += 1
    print('\nfinished with', errors, 'error(s)')

parser = argparse.ArgumentParser(description='renaming multiple folders and/or files at once', epilog='phase 1: preview changes \nphase 2: make changes\n ', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--files', action='store_true', help='run for files')
parser.add_argument('--folders', action='store_true', help='run for folders')
parser.add_argument('-p', metavar='path',  nargs=1, required=True, help='root path (required)')
parser.add_argument('-d', metavar='depth', type=int, nargs=1, default=0, help='specify the depth to traverse, default is 0')
parser.add_argument('-l', action='store_true', help='makes all characters lowercase')
parser.add_argument('-U', action='store_true', help='makes all characters uppercase')
parser.add_argument('-r', nargs=2, metavar=('old', 'new'), default=('',''), help='replaces substring old with new')
args = parser.parse_args()

replacements = list()
replacements.append(args.r)

preview(args.files, args.folders, args.p[0], args.d[0], args.l, args.U, replacements)

q = input('\nAre you sure you want to do this? \nType \'yes\' or \'no\': ')
if q == 'yes':
    execute_change(args.files, args.folders, args.p[0], args.d[0], args.l, args.U, replacements)
