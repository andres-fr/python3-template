# usage example: ./make_sphinx_docs "compuglobalhypermeganet" "Homer Simpson"
# FOR THE MOMENT ONLY CALLABLE FROM REPO ROOT
PACKAGE_NAME=$1
AUTHOR=$2
REPO_ROOT
rm -r docs/
version=`grep "current_version" .bumpversion.cfg | cut -d'=' -f2 | xargs`
sphinx-quickstart -q -p "`echo $PACKAGE_NAME`" -a "`echo $AUTHOR`" --makefile --batchfile --ext-autodoc --ext-mathjax --ext-viewcode --ext-githubpages  -d version="`echo $version`" -d release="`echo $version`" docs/
# sadly the following is needed to change the html_theme flag
sed -i '/html_theme/d' docs/conf.py # remove the html_theme line
sed -i '1r ci_scripts/sphinx_doc_config.txt' docs/conf.py # add the desired config after line 1
echo "" >> docs/conf.py # add newline at EOF to pass flake8
sphinx-apidoc -f "`echo $PACKAGE_NAME`" -o docs/
make -C docs clean && make -C docs latexpdf && make -C docs html
