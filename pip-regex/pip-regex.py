import os
import sys
import pip
import requests
import re
import xmlrpc.client as xmlrpclib

class pipSearch:
  def __init__(self):
      self.client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
  def regex_pip_search(query):
    pkg_list = client.list_packages()
    results = []
    for pkg in pkg_list:
      if re.match(query, pkg) is not None:
        print(client.package_releases(pkg))
        print(pkg)
        if client.package_releases(pkg) print(client.package_releases(pkg)[0]) else pass
        pkg_info = client.release_data(pkg, client.package_releases(pkg))
        results.append({'name': pkg_info['name'],
                        'summary': pkg_info['summary'],
                        'version': pkg_info['version']
        })
        return results


if __name__ == "__main__":
  client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
