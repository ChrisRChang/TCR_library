#### general
################################################################################

RAND_SEED = 100

#### data file locations
################################################################################


# RESTRICTSITES_FN = DATA_DIR+'/restriction_sites.fasta'


#### external data settings
################################################################################

# minimum netphos score above which annotation is carried through
NETPHOS_SCORE_CUTOFF = 0.75





#### 5' barcode chip sequence parameters
################################################################################

'''
{fwd_primer} {seq_barcode} CGAAGGAGACGTCTCCCTGC {domain_seq} AGAGTG {rev_primer}
GTTG ...UMI... ...FWD_PRIMER... ...BC... GCAA..BSMBIx2..CTGC ..LIBRARY.. AGAG(GT) ...REV_PRIMER...
                                            (contains:)
                                        || promo scfv tm ||
'''

CHIP_SEQ_FMT = (
    '{fwd_primer} {seq_barcode} ' +
    'CGAAGGAGACGTCTCCCTGC {domain_seq} AGAGTG {rev_primer}')

OLIGO_CHECK_PRE = 'GTCTCCCTGC'
OLIGO_CHECK_POST = 'AGAGTG'

CHIP_BARCODE_LEN = 9
# length of chip before start of codons
CHIP_5PRIME_LEN = PRIMER_LEN + CHIP_BARCODE_LEN + len('CGAAGGAGACGTCTCCCTGC')
# length of chip after end of codons
CHIP_3PRIME_LEN = len('AGAGTG') + PRIMER_LEN
CHIP_BSMBI_SITES = (
    (
        PRIMER_LEN+CHIP_BARCODE_LEN+5,
        PRIMER_LEN+CHIP_BARCODE_LEN+11
    ),
    (
        PRIMER_LEN+CHIP_BARCODE_LEN+len('CGAAGGAGACGTCTCCCTGC')-11,
        PRIMER_LEN+CHIP_BARCODE_LEN+len('CGAAGGAGACGTCTCCCTGC')-6
    )
)
CHIP_MAX_LEN = 230

# positions and sequences (including overhangs) of domain cutsites
# at 5' and 3' ends of domains
DOM_5P_CUT = (
    (29, 35, (24, 35, 'CGAAGgagacg'.upper())),
    (33, 39, (33, 44, 'cgtctcCCTGC'.upper())),
)
DOM_3P_CUT = (
    (-16, -10, (-21, -10, 'AGAGTgagacc'.upper())),
)

DOM_BC_SPAN = (15, 24)

#### 3' knock-in barcode chip sequence parameters
################################################################################

'''
{fwd_primer} CACTGC {domain_seq} AGAGGGAGACGTCTCCGCCT {seq_barcode} {rev_primer}
...FWD_PRIMER... (CA)CTGC ..LIBRARY.. AGAG..BSMBx2..GCCT ...BC... ...REV_PRIMER... ...UMI...
                                        (contains:)
                                   || zeta 2a marker 2a ||
'''

class KI_CHIP_CFG:
    '''
    chip layout for knockin library version.
    reverse and fwd primer are switched so that the REV_PRIMER_PREFIX is actually the
    FWD_PRIMER_PREFIX.
    '''

    CHIP_SEQ_FMT = (
        '{fwd_primer} CACTGC {domain_seq} ' +
        'AGAGGGAGACGTCTCCGCCT {seq_barcode} {rev_primer}')

    OLIGO_CHECK_PRE = 'CACTGC'
    OLIGO_CHECK_POST = 'AGAGGG'

    CHIP_BARCODE_LEN = 9
    # length of chip before start of codons
    CHIP_5PRIME_LEN = PRIMER_LEN + len('CACTGC')
    # length of chip after end of codons
    CHIP_3PRIME_LEN =  len('AGAGGGAGACGTCTCCGCCT') + CHIP_BARCODE_LEN + PRIMER_LEN

    # bsmbI site spans are inverted b/c orientation of barcode is flipped.
    CHIP_BSMBI_SITES = (
        (
            -(PRIMER_LEN+CHIP_BARCODE_LEN+5),
            -(PRIMER_LEN+CHIP_BARCODE_LEN+11)
        ),
        (
            -(PRIMER_LEN+CHIP_BARCODE_LEN+len('AGAGGGAGACGTCTCCGCCT')-11),
            -(PRIMER_LEN+CHIP_BARCODE_LEN+len('AGAGGGAGACGTCTCCGCCT')-6)
        )
    )
    CHIP_MAX_LEN = 230

    # positions and sequences (including overhangs) of domain cutsites
    # at 5' and 3' ends of domains
    DOM_5P_CUT = (
        (29, 35, (24, 35, 'CGAAGgagacg'.upper())),
        (33, 39, (33, 44, 'cgtctcCCTGC'.upper())),
    )
    DOM_3P_CUT = (
        (-16, -10, (-21, -10, 'AGAGTgagacc'.upper())),
    )
    DOM_BC_SPAN = (15, 24)

#### shuffled motif settings
################################################################################
SHUF_UNIPROT_MOTIFS = [
    'Box 1',
    'ITIM',
    'ITSM',
    'Interaction with GRB2',
    'Interaction with SRC and ESR1',
    'LIR',
    'NPXY',
    'PDZ-binding',
    'PDZ-binding (in isoform 2)',
    'PPPSP',
    'PPXY',
    'PPxY',
    'PTB-like',
    'SH2-binding',
    'SH3-binding',
    'SLAM-like']

SHUF_ELM_MOTIFS = [
    'SH2',
    'SH3',
    'MAPK',
    'WIRS',
    'TRAF',
    'ITAM',
    'ITSM',
    'ITIM',
    'PTB',
    'PDZ',
    'Actin',
    'PP2A',
    'PKB']

# number of occurrences oer chunk
SHUF_REP_CHUNKS = 6
# required num fwd
SHUF_REP_START_CHUNKS = 2
# required num rev
SHUF_REP_END_CHUNKS = 2

SHUF_MAX_AA_LEN = 50
SHUF_MIN_AA_LEN = 25

#### chip mut settings
################################################################################
PHOSPHO_RESIDUES = ['Y','T','S']
PHOSPHOMIM_RESIDUE = 'D'

#### mutate settings
################################################################################

# how long a domain has to be, in multiples of
# `AA_CHUNK_SIZE`, in order to be considered large
LARGE_DOMAIN_MULTI = 2

# minimum final window step - if smaller, delete
# second to last chunk (to prevent similar final 2 chunks)
MIN_WINFINALSTEP = 11

# very important domains to do extra stuff to
VIP_DOMAINS = [
    'OX40',
    'ICOS',
    '4-1BB',
    'CTLA4',
    'CD28',
    'CD30'
]

# operations to perform on all curated domains
BASE_OP_TYPES = [
    'phos_ko',
    'del_scan',
    'ubi_ko',
    'wt'
]

# operations to additionally perform on very small domains
SMALL_OP_TYPES = [
    'var',
    'phos_act',
]

# operations to perform on noncurated domains
NONCURATED_OP_TYPES = [
    'wt'
]

DEFAULT_MUT_CFG = {
    'AA_CHUNK_SIZE': 55,
    'AA_CHUNK_SHIFT': 22,
    'ALA_SCAN_SIZE': 6,
    'ALA_SCAN_SHIFT': 3,
    'NUM_PHOS_AA_CUTOFF': 0,
    'op_types' : BASE_OP_TYPES
}

VIP_OP_TYPES = [
    #'phos_multiko',
    'sbp',
    'del',
    'ins'
]

# number of single-aa shuffled domains to generate for each VIP domain
# as negative controls
N_SHUFFLE_DOMAIN_REPS = 5

# Maximum size of domains to include that are not curated
MAX_NONCURATED_SIZE = DEFAULT_MUT_CFG['AA_CHUNK_SIZE'] * 8

# Note: If oligos are synthesized too small, then they will be removed with
# SPRI beads, which we do not want. CD80/B71 is the smallest annotated domain
# besides TREM1 and CD300e, and its 25, so 25*3 + 54bp for the UMI and
# cutsites is 129. We can go down to 100bp oligo lengths, which is 15 aa.
# There might be an issue with preferential amplification of these shorter
# guys, but we think that processivity differences below ~500 bp should be
# negligible. ~ dbg

MIN_DOMAIN_SIZE = 15

LIBRARY_SUMMARY_CSV_OUT_FN = OUTFILE_DIR + 'tcsl_lib_summary.csv'

LIBRARY_CSV_OUT_FN = OUTFILE_DIR + 'tcsl_lib_'