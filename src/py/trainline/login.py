import os

from chromedriver_utils.init import init


PARENT_DIR = os.path.dirname(__file__)
PY_ROOT = os.path.join(PARENT_DIR, os.pardir)
CHROMEDRIVER_PATH = os.path.join(PY_ROOT, "chromedriver")


def login():
    driver = init(CHROMEDRIVER_PATH)


if __name__ == "__main__":
    login()
