def entry_type(entry):
    pos_at = entry.find('@')
    pos_first_bracket = entry.find('{')
    return(entry[pos_at+1:pos_first_bracket])

def get_key(entry):
    pos_first_bracket = entry.find('{')
    #We know that the key is after the '{' until the ','
    pos_first_comma = entry.find(',')
    return(entry[pos_first_bracket+1:pos_first_comma])


def get_entries(entry):
    position = entry.find(',')
    #We are interested every thing after '@Article{key,'
    entry = entry[position:]
    return_list = []
    at_end_of_entry = False
    while(not at_end_of_entry):
        #If there is only a closing '}'  and no '{' then we are at the
        #end of the entry.
        if entry.find('{') == -1:
            at_end_of_entry = True
        else:
            #We consume the string use parition to get every thing before and
            #after the '='. The stuff before is the field name.
            (field_name, __dont_care , entry) = entry.partition('=')
            (stuff,entry) = find_stuff(entry)
            return_list.append((field_name.strip(' \n,'),stuff))
    return(return_list)

def find_stuff(entry):
    start_pos = entry.find('{')+1
    position = start_pos
    #The goal is to find the a mathcing '}' in the string.
    #But we need to keep track of the bracket level.
    #We assume that the string does have a closing '}' and the
    #brackets match. No error checking is done. I assume that
    #the entry is well formed.
    bracket_level = 1
    while(bracket_level != 0):
        if entry[position] == '{':
            bracket_level = bracket_level + 1
        if entry[position] == '}':
            bracket_level = bracket_level - 1
        position = position + 1
    stuff = entry[start_pos:position-1]
    rest = entry[position:]
    return (stuff.strip('\n '),rest)
    
