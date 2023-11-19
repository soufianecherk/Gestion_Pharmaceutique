import dbf

table = dbf.Table('apo_clie', 'NOM C(30); ADRESSE C(30); NUMCL N(4,0); PHARMACIEN C(30); CREDIT N(4,2)')
table.open(dbf.READ_WRITE)