import pytest
import glob, os, sys


def check_columun_count():
    for path in glob.glob(__file__ + "/*"):
        if path.find(".") == -1 and os.path.isfile(path):
            lines = []
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            sample_args = 0
            for line in lines:
                if not line.startswith("#"):
                    meta_args = len(line.split(","))
                    if sample_args == 0:
                        sample_args = meta_args
                    assert sample_args == meta_args
