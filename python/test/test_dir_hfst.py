import hfst

diritems = \
['EPSILON', 
 'HfstBasicTransducer', 'HfstBasicTransition', 'HfstInputStream', 'HfstOutputStream', 
 'HfstTokenizer', 'HfstTransducer', 'IDENTITY', 'LexcCompiler', 'PmatchContainer', 
 'TO_FINAL_STATE', 'TO_INITIAL_STATE', 'UNKNOWN', 
 'XfstCompiler', 'XreCompiler', 'compile_lexc_file', 
 'compile_pmatch_expression', 'compile_pmatch_file', 'compile_xfst_file', 'concatenate', 'disjunct', 
 'empty_fst', 'epsilon_fst', 'exceptions', 'fsa', 'fst', 'fst_type_to_string', 'get_default_fst_type', 
 'get_output_to_console', 'intersect', 'is_diacritic', 
 'read_att_input', 'read_att_string', 'regex', 'rules', 'set_default_fst_type', 'set_output_to_console', 
 'start_xfst', 'tokenized_fst']

dirhfst = dir(hfst)

for item in diritems:
    if not item in dirhfst:
        print('error: dir(hfst) does not contain', item)
        assert(False)

assert hfst.EPSILON == '@_EPSILON_SYMBOL_@'
assert hfst.UNKNOWN == '@_UNKNOWN_SYMBOL_@'
assert hfst.IDENTITY == '@_IDENTITY_SYMBOL_@'

assert hfst.types.SFST_TYPE == 0
assert hfst.types.TROPICAL_OPENFST_TYPE == 1
assert hfst.types.LOG_OPENFST_TYPE == 2
assert hfst.types.FOMA_TYPE == 3
assert hfst.types.XFSM_TYPE == 4
assert hfst.types.HFST_OL_TYPE == 5
assert hfst.types.HFST_OLW_TYPE == 6
assert hfst.types.HFST2_TYPE == 7
assert hfst.types.UNSPECIFIED_TYPE == 8
assert hfst.types.ERROR_TYPE == 9

assert hfst.TO_INITIAL_STATE == 0
assert hfst.TO_FINAL_STATE == 1
