from happana.template import HapPAnaBase
from collections import OrderedDict


class Marker(object):
    """

    to keep information of one marker

    """

    def __init__(self, code):
        self.__code = code
        self.chrom = None
        self.pos = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<Marker Object> ' + str(self.get_raw_repr())

    def get_raw_repr(self):
        return {'Code': self.code,
                'Chromosome': self.chrom,
                'Position': self.pos,
                }

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def chrom(self):
        return self.__chrom

    @chrom.setter
    def chrom(self, value):
        self.__chrom = value

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        self.__pos = value


class Base(object):
    """

    to keep information of one allele

    """

    def __init__(self, marker):
        self.__marker = marker
        self.nucleotide = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<Base Object> ' + str(self.get_raw_repr())

    def get_raw_repr(self):
        return {'Marker': self.__marker,
                'nucleotide': self.nucleotide,
                }

    @property
    def marker(self):
        return self.__marker

    @property
    def nucleotide(self):
        return self.__nucleotide

    @nucleotide.setter
    def nucleotide(self, value):
        self.__nucleotide = value


class PlinkStats(object):
    """

    PLINK Statistics

    """

    def __init__(self):
        self.f_a = None
        self.f_u = None
        self.chisq = None
        self.or_val = None
        self.p_val = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<PlinkStats Object> ' + str(self.get_raw_repr())

    def get_raw_repr(self):
        return {'Affected frequency': self.f_a,
                'Unaffected frequency': self.f_u,
                'Chisq': self.chisq,
                'OR value': self.or_val,
                'P value': self.p_val,
                }


class PlinkRegion(object):
    """

    PLINK region with specific statistics values

    """

    def __init__(self, plink_stats):
        self.__stats = plink_stats
        self.__bases = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<PlinkRegion Object> ' + str(self.get_raw_repr())

    def get_raw_repr(self):
        return {'Window size': self.size,
                'PLINK statistics': self.stats,
                'Bases': self.bases,
                }

    @property
    def size(self):
        return len(self.bases)

    @property
    def stats(self):
        return self.__stats

    @property
    def bases(self):
        return self.__bases

    def add_base(self, base):
        self.__bases.append(base)


#class Genotype(object):
#    """
#
#    to keep genotype information at one position
#
#    Usage:
#        either through as an argument through Constructor or
#        assigning it through 'raw' property
#
#    """
#
#    def __init__(self, marker, position, raw_genotype):
#        self.__marker = marker
#        self.__position = position
#        self.raw_genotpye = raw_genotype
#
#    def __str__(self):
#        return self.__repr__()
#
#    def __repr__(self):
#        return '<Genotype Object> ' + str(self.get_raw_repr())
#
#    def get_raw_repr(self):
#        return {'Marker': self.__marker,
#                'Position': self.__position,
#                'Raw genotype': self.raw_genotype,
#                'Size': self.size,
#                'first base': self.first_base,
#                'second base': self.second_base,
#                }
#
#    @property
#    def raw_genotype(self):
#        return self.__raw_genotype
#
#    @raw_genotype.setter
#    def raw_genotype(self, value):
#        self.__raw_genotype = value
#        tmp_bases = value.split('/')
#        tmp_bases.sort()
#        self.__size = len(tmp_bases)
#        if self.__size <> 2:
#            self.__first_base = None
#            self.__second_base = None
#        else:
#            self.__first_base = tmp_bases[0]
#            self.__second_base = tmp_bases[1]
#
#    @property
#    def size(self):
#        return self.__size
#
#    @property
#    def first_base(self):
#        return self.__first_base
#
#    @property
#    def second_base(self):
#        return self.__second_base
#
#
#class PatientGenotypeRecord(object):
#    """
#
#    to keep whole genotype information for one patient
#
#    """
#
#    def __init__(self, patient_code):
#        self.__patient_code = patient_code
#        self.__genotype = OrderedDict()
#
#    def __str__(self):
#        return self.__repr__()
#
#    def __repr__(self):
#        return '<PatientGenotypeRecord Object> ' + str(self.get_raw_repr())
#
#    def get_raw_repr(self):
#        return {'Patient code': self.raw_genotype,
#                'Genotype': self.size,
#                'first_base base': self.first_base,
#                'second_base base': self.second_base,
#                }
#
#    def get_genotype_repr(self):
#        return None
#
#    @property
#    def genotype(self):
#        return self.__genotype
