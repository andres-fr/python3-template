# usage example: ./make_sphinx_docs "compuglobalhypermeganet" "Homer Simpson"
# FOR THE MOMENT ONLY CALLABLE FROM REPO ROOT

PACKAGE_NAME=$1
AUTHOR=$2
VERSION=`grep "current_version" .bumpversion.cfg | cut -d'=' -f2 | xargs`
CONF_PY_PATH="docs/conf.py"
rm -rf docs/*

sphinx-quickstart -q -p "$PACKAGE_NAME" -a "$AUTHOR" --makefile --batchfile --ext-autodoc --ext-imgmath --ext-viewcode --ext-githubpages  -d version="$VERSION" -d release="$VERSION" docs/

# sadly the following is needed to change the html_theme flag
sed -i '/html_theme/d' "$CONF_PY_PATH" # remove the html_theme line
sed -i '1r ci_scripts/sphinx_doc_config.txt' "$CONF_PY_PATH" # add the desired config after line 1
echo -e "\nlatex_elements = {'extraclassoptions': 'openany,oneside'}" >> "$CONF_PY_PATH" # override latex config at end of file to minimize blank pages

# even more sadly, this is the cleanest way I found to allow apidoc edit
# index.rst without altering conf.py:
rm docs/index.rst
sphinx-apidoc -F "$PACKAGE_NAME" -o docs/

make -C docs clean && make -C docs latexpdf && make -C docs html
