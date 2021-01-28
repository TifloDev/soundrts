#! .venv\Scripts\python.exe
import os
import shutil
from os.path import join

from docutils import core

import rules2doc

SRC = "doc_src/src"


def build(dest="."):
    DEST = join(dest, "doc")
    try:
        os.makedirs(DEST)
    except OSError:
        pass

    for lang in ("en", "ru"):
        p = join(SRC, lang)
        dp = join(DEST, lang)
        open(join(p, "stats.inc"), "w").write(rules2doc.stats)
        try:
            os.mkdir(dp)
        except OSError:
            pass
        for n in os.listdir(p):
            if n.endswith(".rst"):
                core.publish_file(
                    source_path=join(p, n),
                    writer_name="html",
                    destination_path=join(dp, n[:-3] + "htm"),
                )


if __name__ == "__main__":
    build()
