# MIPS Disassembler

funct_code_table = {
    '100000': 'add',
    '100100': 'and',
    '001000': 'jr',
    '100011': 'lw',
    '001101': 'ori',
    '100010': 'sub',
    '101011': 'sw'
}

register_table = {
    '00000': '$zero',
    '00001': '$at',
    '00010': '$v0',
    '00011': '$v1',
    '00100': '$a0',
    '00101': '$a1',
    '00110': '$a2',
    '00111': '$a3',
    '01000': '$t0',
    '01001': '$t1',
    '01010': '$t2',
    '01011': '$t3',
    '01100': '$t4',
    '01101': '$t5',
    '01110': '$t6',
    '01111': '$t7',
    '10000': '$s0',
    '10001': '$s1',
    '10010': '$s2',
    '10011': '$s3',
    '10100': '$s4',
    '10101': '$s5',
    '10110': '$s6',
    '10111': '$s7',
    '11000': '$t8',
    '11001': '$t9',
    '11010': '$k0',
    '11011': '$k1',
    '11100': '$gp',
    '11101': '$sp',
    '11110': '$fp',
    '11111': '$ra',
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
    fields = {}
    fields['binary'] = instruction['binary']
    fields['opcode'] = instruction['binary'][0:6]
    fields['rs'] = instruction['binary'][6:11]
    fields['rt'] = instruction['binary'][11:16]
    fields['rd'] = instruction['binary'][16:21]
    fields['shamt'] = instruction['binary'][21:26]
    fields['funct'] = instruction['binary'][26:]
    instruction_string = funct_code_table[fields['funct']]
    instruction_string += f' {register_table[fields["rd"]]}, {register_table[fields["rs"]]}, {register_table[fields["rt"]]}'
    fields['MIPS'] = instruction_string
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
