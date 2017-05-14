#!/usr/bin/env python
# _*_coding:utf-8_*_

import os
import ConfigParser

__author__ = 'Sheng Chen'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.default_path = os.path.join(BASE_DIR, 'conf/default.ini')
        self.default_parser = ConfigParser.ConfigParser()
        self.default_parser.read(self.default_path)

    @property
    def parser(self):
        cp = ConfigParser.ConfigParser()
        if os.path.exists(self.conf_path):
            pass
        else:
            conf_path = os.path.join(BASE_DIR, 'conf')
            print "INFO: Not Found config file [%s], use [%s] instead" % \
                  (self.conf_path,
                   os.path.join(conf_path, 'default.ini'))
            self.conf_path = self.default_path
        cp.read(self.conf_path)
        return cp

    @property
    def sections(self):
        cf = ConfigParser.ConfigParser()
        cf.read(self.conf_path)
        return cf.sections()

    @property
    def mysql_options(self):
        return self.parser.options('mysql')

    @property
    def mysql_port(self):
        if 'port' in self.mysql_options:
            return self.parser.get('mysql', 'port')
        else:
            return self.default_parser.get('mysql', 'port')

    @property
    def mysql_host(self):
        if 'host' in self.mysql_options:
            return self.parser.get('mysql', 'host')
        else:
            return self.default_parser.get('mysql', 'host')

    @property
    def mysql_db_name(self):
        if 'db_name' in self.mysql_options:
            return self.parser.get('mysql', 'db_name')
        else:
            return self.default_parser.get('mysql', 'db_name')

    @property
    def mysql_user(self):
        if 'user' in self.mysql_options:
            return self.parser.get('mysql', 'user')
        else:
            return self.default_parser.get('mysql', 'user')

    @property
    def mysql_password(self):
        if 'password' in self.mysql_options:
            return self.parser.get('mysql', 'password')
        else:
            return self.default_parser.get('mysql', 'password')

config = Config(os.path.join(BASE_DIR, 'conf/cmdb.ini'))

if __name__ == '__main__':
    print config.mysql_host
