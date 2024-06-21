import setuptools

with open("README.md","r",encoding="utf=8") as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="Text-Summarization"
AUTHOR_USER_NAME="Sneha7382"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL="snehalathauddatla@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is a Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sneha7382/Text-Summarization",
    project_urls={
        "BugTracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
   
)