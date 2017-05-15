# coding=utf-8

import os
import ConfigParser

__author__ = 'Sheng Chen'


class Config(object):
    def __init__(self, conf_dir, conf_file):
        self.conf_dir = conf_dir
        self.conf_file = conf_file
        self.default_path = os.path.join(self.conf_dir, 'default.ini')
        self.cp = ConfigParser.ConfigParser()
        if not os.path.exists(self.conf_file):
            print "INFO: Not Found config file [%s], use [%s] instead" % (
                os.path.join(self.conf_dir, self.conf_file),
                self.default_path
                )
            self.conf_file = self.default_path
        self.cp.read(self.conf_file)

    def conf_sections(self):
        return self.cp.sections()

    def conf_options(self, section):
        if section in self.conf_sections():
            return self.cp.options(section)
        else:
            print "%s have no conf section %s" % (self.conf_file, section)

    def get_config(self, section, option):
        if option in self.conf_options(section):
            return self.cp.get(section, option)

    def conf(self, section):
        conf_result = {}
        for option in self.conf_options(section):
            conf_result[option] = self.get_config(section, option)
        return conf_result
