# MIPS Disassembler

funct_code_table = {
    '100000': 'add',
    '100100': 'and',
    '000010': 'j',
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

hex_dict = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
}


def binary_to_hex(binary):
    hex_str = ''
    count = -4
    prev = len(binary)
    byte = binary[-4:prev]

    while abs(count) <= len(binary):
        byte = binary[count:prev]
        hex_str = hex_dict[byte] + hex_str
        prev = count
        count -= 4

    hex_str = '0x' + hex_str

    return hex_str


def process_r_type(instruction):
    fields = {}
    fields['binary'] = instruction['binary']
    fields['opcode'] = instruction['binary'][0:6]
    fields['funct'] = instruction['binary'][26:]

    instruction_string = funct_code_table[fields['funct']]

    if funct_code_table[fields['funct']] == 'jr':
        fields['ra'] = instruction['binary'][6:11]
        instruction_string += f' {register_table[fields["ra"]]}'
    else:
        fields['rs'] = instruction['binary'][6:11]
        fields['rt'] = instruction['binary'][11:16]
        fields['rd'] = instruction['binary'][16:21]
        fields['shamt'] = instruction['binary'][21:26]
        instruction_string += f' {register_table[fields["rd"]]}, {register_table[fields["rs"]]}, {register_table[fields["rt"]]}'

    fields['MIPS'] = instruction_string
    # print(fields)
    return fields


def process_i_type(instruction):
    fields = {}
    fields['binary'] = instruction['binary']
    fields['opcode'] = instruction['binary'][0:6]
    fields['rs'] = instruction['binary'][6:11]
    fields['rt'] = instruction['binary'][11:16]
    fields['immediate'] = instruction['binary'][16:]

    instruction_string = funct_code_table[fields['opcode']]
    if funct_code_table[fields['opcode']] == 'ori':
        instruction_string += f' {register_table[fields["rt"]]}, {register_table[fields["rs"]]}, {binary_to_hex(fields["immediate"])}'
    else:
        instruction_string += f' {register_table[fields["rt"]]}, {binary_to_hex(fields["immediate"])}({register_table[fields["rs"]]})'

    fields['MIPS'] = instruction_string
    # print(fields)

    return fields


def process_j_type(instruction):
    fields = {}
    fields['binary'] = instruction['binary']
    fields['opcode'] = instruction['binary'][0:6]
    fields['address'] = instruction['binary'][6:]
    instruction_string = f'{funct_code_table[fields["opcode"]]} {binary_to_hex(fields["address"])}'
    fields['MIPS'] = instruction_string
    return fields


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
for i, result in enumerate(results):
    print(f'{i+1}. {result}')
