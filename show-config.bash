cat << EOF >> ~/.pypirc
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
repository: https://pypi.python.org/pypi
username: ${#PYPI_USERNAME}
EOF

cat ~/.pypirc
