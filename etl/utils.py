import os
import requests
import re
import zipfile
import datetime
import shutil
from sqlalchemy import text


def create_directory(directory, delete_first=False):
    try:
        if(delete_first):
            remove_directory(directory)

        if not os.path.isdir(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def remove_directory(directory):
    try:
        if os.path.isdir(directory):
            shutil.rmtree(directory)
    except OSError:
        print('Error: Removing directory. ' + directory)


def fetch_file(url, directory, filename=None):
    r = requests.get(url)
    # print(r)
    """
    SET FILENAME TO DOWNLOADED FILE NAME
    """
    # print('-> ', hasattr(r.headers, 'content-disposition'))
    if not (filename):
        if(hasattr(r.headers, 'content-disposition')):
            d = r.headers['content-disposition']
            filename = re.findall(
                "filename=(.+)", d)[0]
        else:
            filename = f"extract_file_{datetime.datetime.now().replace(microsecond=0).isoformat()}.zip"

    file_path = directory + filename
    with open(f"{file_path}", "wb") as code:
        code.write(r.content)

        return filename


def get_filename_from_url(url, type=".zip"):
    fn = url.split('/')
    fn.reverse()
    return fn[0] if fn[0].endswith(type) else None


def unzip(from_path, to_dir="."):
    with zipfile.ZipFile(from_path, 'r') as zip:
        zip.printdir()

        zip.extractall(path=to_dir)


def rename_files(files_list, src_dir, dest_dir):
    # print("rename_files", files_list, src_dir, dest_dir)
    for i, file in enumerate(files_list):
        src = src_dir+file['src_path']
        dest = dest_dir+file['dest_path']

        if os.path.exists(src):
            os.rename(src, dest)


def downcase(word):
    return word[:1].lower() + word[1:] if word else ''


def make_table_name(orig): return orig.replace(
    ' ', '_').replace('-', '_').lower()


def str2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")


def prefixify(name, prefix):
    # if(not name.startswith(prefix)):
    return prefix + name

    # return name


def tablenamify(name, prefix):
    return f"{prefix + name}_table" if prefix else f"{name}_table"
    # return prefixify(name + "_table", prefix)


def viewnameify(name, prefix, translations):
    if (name in translations['tables']['noprefix']):
        return name

    return f"{prefix + name}"


def execute_sql(engine, statement):
    with engine.connect() as conn:
        conn.execute(text(statement))


def pretty_print(text, is_bullet=False):

    if(not is_bullet):
        output = f"\n--- {text.upper()}"
    else:
        output = f"    * {text}"

    print(output)


def get_num_files_in_dir(dir):
    return len([name for name in os.listdir(dir)])


def clean_and_join_list(mylist, separator="_"):
    return separator.join([x.lower() for x in mylist if len(x)])
