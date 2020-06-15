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

instruction_list = [
    {
        'binary': '00000001101011100101100000100100',
        'type': 'R'
    },
    {
        'binary': '10001101010010010000000000001000',
        'type': 'I'
    },
    {
        'binary': '00001000000000010010001101000101',
        'type': 'J'
    },
    {
        'binary': '00000010101010010101100000100010',
        'type': 'R'
    },
    {
        'binary': '00000011111000000000000000001000',
        'type': 'R'
    },
    {
        'binary': '00110101111100001011111011101111',
        'type': 'I'
    },
    {
        'binary': '10101110100011010000000000100000',
        'type': 'I'
    },
    {
        'binary': '00000010110011010101000000100000',
        'type': 'R'
    }
]


def process_r_type(instruction):
    print(instruction)
    fields = {}
    fields['opcode'] = instruction['binary'][0:6]
    fields['rs'] = instruction['binary'][6:11]
    fields['rt'] = instruction['binary'][11:16]
    fields['rd'] = instruction['binary'][16:21]
    fields['shamt'] = instruction['binary'][21:26]
    fields['funct'] = instruction['binary'][26:]

    print(fields)


def process_i_type(instruction):
    # print(instruction)
    pass


def process_j_type(instruction):
    # print(instruction)
    pass


def sort_instructions(instruction_list):
    results = []
    for instruction in instruction_list:
        if (instruction['type'] == 'R'):
            results.append(process_r_type(instruction))
        if (instruction['type'] == 'I'):
            results.append(process_i_type(instruction))
        if (instruction['type'] == 'J'):
            results.append(process_j_type(instruction))
    return results


results = sort_instructions(instruction_list)
