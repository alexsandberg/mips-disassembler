# MIPS Disassembler

code_table = {
    'add': {
        'opcode': '000000',
        'funct': '100000'
    },
    'and': {
        'opcode': '000000',
        'funct': '100100'
    },
    'j': {
        'opcode': None,
        'funct': None
    },
    'jr': {
        'opcode': '000000',
        'funct': '001000'
    },
    'lw': {
        'opcode': None,
        'funct': '100011'
    },
    'ori': {
        'opcode': None,
        'funct': '001101'
    },
    'sub': {
        'opcode': '000000',
        'funct': '100010'
    },
    'sw': {
        'opcode': None,
        'funct': '101011'
    }
}
