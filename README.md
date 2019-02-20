=============
ckanext-cob
=============

This is the CKAN theme for the City of Bloomington, Indiana.

------------
Installation
------------
CKAN will only run in development mode.  There is no mechanism for fixed production deployments.  Once you've installed it, make sure to add it to the CKAN configuration's list of enabled plugins.

### Install from Github

This is how we deploy, when we use Ansible.  Ansible pulls down the latest master branch from Github.
```bash
cd /srv/sites/ckan
. bin/activate
pip install -e 'git+https://github.com/City-of-Bloomington/ckanext-cob.git#egg=ckanext-cob'
sudo service apache2 stop
sudo service apache2 start
```

### Install locally built version
If you are working on the theme locally, and want to install it into an existing CKAN installation, you replace the directory, then put the newly copied version into development mode.
```bash
cd /srv/sites/ckan
. bin/activate
cd src/ckanext-cob
python setup.py develop
sudo service apache2 stop
sudo service apache2 start
```
