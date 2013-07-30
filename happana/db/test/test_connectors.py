import os
import csv
from happana.db.test.template import SafeDBTester
from happana.db.connectors import VinayPlinkDB


class TestVinayPlinkDB(SafeDBTester):

    def __init__(self, test_name):
        SafeDBTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'VinayPlinkDB'

    def __create_db_instance(self):
        db = VinayPlinkDB()
        return db

    def test_usage(self):
        """ to check VinayPlinkDB can be used in the most common scenario """

        self.init_test(self.current_func_name)
        db = self.__create_db_instance()
        test_file = os.path.join(self.data_dir,
                                 self.current_func_name + '.xlsx')
        db.open_db(test_file)
        self.assertEqual(db.nmarkers,
                         40,
                         'Incorrect number of markers loaded')
        self.assertEqual(db.nwindows,
                         19,
                         'Incorrect number of windows loaded')
        windows = db.windows()
        test_window = windows.next()
        self.assertEqual(test_window.stats.f_a,
                         0.02371,
                         'Incorrect f_a value')
        self.assertEqual(test_window.stats.f_u,
                         0.0109,
                         'Incorrect f_u value')
        self.assertEqual(test_window.stats.chisq,
                         6.4,
                         'Incorrect chisq value')
        self.assertEqual(test_window.stats.or_val,
                         2.20377076257891,
                         'Incorrect OR value')
        self.assertEqual(test_window.stats.p_val,
                         0.01141,
                         'Incorrect p value')
        self.assertEqual(test_window.size,
                         1,
                         'Incorrect window size')
        self.assertEqual(test_window.bases[0].marker.code,
                         'rs16911887',
                         'Incorrect marker code')
        self.assertEqual(test_window.bases[0].marker.chrom,
                         '9',
                         'Incorrect chromosome')
        self.assertEqual(test_window.bases[0].marker.pos,
                         '97734605',
                         'Incorrect position')
        self.assertEqual(test_window.bases[0].nucleotide,
                         'A',
                         'Incorrect nucleotide')
        test_window = windows.next()
        test_window = windows.next()
        self.assertEqual(test_window.stats.f_a,
                         0.02586,
                         'Incorrect f_a value')
        self.assertEqual(test_window.stats.f_u,
                         0.01336,
                         'Incorrect f_u value')
        self.assertEqual(test_window.stats.chisq,
                         5.041,
                         'Incorrect chisq value')
        self.assertEqual(test_window.stats.or_val,
                         1.96046640371504,
                         'Incorrect OR value')
        self.assertEqual(test_window.stats.p_val,
                         0.02476,
                         'Incorrect p value')
        self.assertEqual(test_window.size,
                         1,
                         'Incorrect window size')
        self.assertEqual(test_window.bases[0].marker.code,
                         'rs7866661',
                         'Incorrect marker code')
        self.assertEqual(test_window.bases[0].marker.chrom,
                         '9',
                         'Incorrect chromosome')
        self.assertEqual(test_window.bases[0].marker.pos,
                         '97749379',
                         'Incorrect position')
        self.assertEqual(test_window.bases[0].nucleotide,
                         'C',
                         'Incorrect nucleotide')
        test_window = windows.next()
        test_window = windows.next()
        test_window = windows.next()
        test_window = windows.next()
        self.assertEqual(test_window.stats.f_a,
                         0.02592,
                         'Incorrect f_a value')
        self.assertEqual(test_window.stats.f_u,
                         0.01402,
                         'Incorrect f_u value')
        self.assertEqual(test_window.stats.chisq,
                         4.3670,
                         'Incorrect chisq value')
        self.assertEqual(test_window.stats.or_val,
                         1.87137344623131,
                         'Incorrect OR value')
        self.assertEqual(test_window.stats.p_val,
                         0.03665,
                         'Incorrect p value')
        self.assertEqual(test_window.size,
                         5,
                         'Incorrect window size')
        self.assertEqual(test_window.bases[0].marker.code,
                         'rs6479565',
                         'Incorrect marker code')
        self.assertEqual(test_window.bases[0].marker.chrom,
                         '9',
                         'Incorrect chromosome')
        self.assertEqual(test_window.bases[0].marker.pos,
                         '97476866',
                         'Incorrect position')
        self.assertEqual(test_window.bases[0].nucleotide,
                         'G',
                         'Incorrect nucleotide')
        self.assertEqual(test_window.bases[4].marker.code,
                         'rs3802462',
                         'Incorrect marker code')
        self.assertEqual(test_window.bases[4].marker.chrom,
                         '9',
                         'Incorrect chromosome')
        self.assertEqual(test_window.bases[4].marker.pos,
                         '97522464',
                         'Incorrect position')
        self.assertEqual(test_window.bases[4].nucleotide,
                         'G',
                         'Incorrect nucleotide')
