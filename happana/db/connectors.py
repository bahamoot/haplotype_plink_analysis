import xlrd
from happana.template import HapPAnaBase
from happana.db.base_classes import Marker
from happana.db.base_classes import Base
from happana.db.base_classes import PlinkStats
from happana.db.base_classes import PlinkRegion
from collections import OrderedDict

VINAY_PLINK_1ST_MARKER_IDX = 6
MARKER_COLS = 3
VINAY_PLINK_MARKER_COL_IDX = 0
VINAY_PLINK_CHROM_COL_IDX = 1
VINAY_PLINK_POS_COL_IDX = 2
VINAY_PLINK_MARKER_F_A_ROW_IDX = 1
VINAY_PLINK_MARKER_F_U_ROW_IDX = 2
VINAY_PLINK_MARKER_CHISQ_ROW_IDX = 3
VINAY_PLINK_MARKER_OR_VAL_ROW_IDX = 4
VINAY_PLINK_MARKER_P_VAL_ROW_IDX = 5


class VinayPlinkDB(HapPAnaBase):
    """

    to keep information of one marker

    """

    def __init__(self):
        HapPAnaBase.__init__(self)
        self.__markers = []
        self.__total_cols = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<VinayPlink Object> ' + str(self.get_raw_repr())

    def get_raw_repr(self):
        return {'Number of Markers': self.nmarkers,
                'Number of Windows': self.nwindows,
                }

    @property
    def nmarkers(self):
        return len(self.__markers)

    @property
    def nwindows(self):
        return self.__total_cols-MARKER_COLS

    def open_db(self, plink_file):
        wb = xlrd.open_workbook(plink_file)
        self.__ws = wb.sheet_by_index(0)
        self.__total_rows = self.__ws.nrows
        self.__total_cols = self.__ws.ncols
        self.__load_markers()

    def __load_markers(self):
        ws = self.__ws
        start_row_idx = VINAY_PLINK_1ST_MARKER_IDX
        #iterate through all marker contents (3 cols)
        for row_idx in xrange(start_row_idx, self.__total_rows):
            marker_code = str(ws.cell_value(row_idx, VINAY_PLINK_MARKER_COL_IDX))
            chrom = ws.cell_value(row_idx, VINAY_PLINK_CHROM_COL_IDX)
            pos = ws.cell_value(row_idx, VINAY_PLINK_POS_COL_IDX)
            mk = Marker(marker_code)
            mk.chrom = '{chrom:.0f}'.format(chrom=chrom)
            mk.pos = '{pos:.0f}'.format(pos=pos)
            self.__markers.append(mk)

    def windows(self):
        start_col_idx = MARKER_COLS
        start_row_idx = VINAY_PLINK_1ST_MARKER_IDX
        ws = self.__ws
        #iterate over all windows
        for col_idx in xrange(start_col_idx, self.__total_cols):
            #get PLINK statistics
            ps = PlinkStats()
            ps.f_a = ws.cell_value(VINAY_PLINK_MARKER_F_A_ROW_IDX, col_idx)
            ps.f_u = ws.cell_value(VINAY_PLINK_MARKER_F_U_ROW_IDX, col_idx)
            ps.chisq = ws.cell_value(VINAY_PLINK_MARKER_CHISQ_ROW_IDX, col_idx)
            ps.or_val = ws.cell_value(VINAY_PLINK_MARKER_OR_VAL_ROW_IDX, col_idx)
            ps.p_val = ws.cell_value(VINAY_PLINK_MARKER_P_VAL_ROW_IDX, col_idx)
            #init PLINK region
            pr = PlinkRegion(ps)
            #search through a single to find the region
            for row_idx in xrange(start_row_idx, self.__total_rows):
                nucleotide = ws.cell_value(row_idx, col_idx)
                if nucleotide <> '':
                    base = Base(self.__markers[row_idx-start_row_idx])
                    base.nucleotide = str(nucleotide)
                    pr.add_base(base)
            yield pr
