import unittest
import os
from happana.template import SafeTester
from happana.template import RiskyTester


class SafeDBTester(SafeTester):
    """ General template for safe "DB" modules testing """

    def __init__(self, test_name):
        SafeTester.__init__(self, test_name)

    def set_dir(self):
        self.working_dir = os.path.join(os.path.join(os.path.join(os.path.dirname(__file__),
                                                                  'tmp'),
                                                     self.test_class),
                                        self.test_function)
        self.data_dir = os.path.join(os.path.join(os.path.dirname(__file__),
                                                  'data'),
                                     self.test_class)


#class RiskyDBTester(RiskyTester):
#    """ General template for risky "DB" modules testing """
#
#    def __init__(self, test_name):
#        RiskyTester.__init__(self, test_name)
#
#    def set_dir(self):
#        self.working_dir = happana_settings.happana_WORKING_DIR
#        self.data_dir = os.path.join(os.path.join(os.path.dirname(__file__),
#                                                  'big_data'),
#                                     self.test_class)
