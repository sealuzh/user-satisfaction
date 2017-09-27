user_metrics = ['PD', 'FR', 'PD + App', 'PD + GUI', 'PD + Contents', 'PD + Pricing',
                'PD + Feature/Functionality', 'PD + Improvement', 'PD + Update/Version', 'PD + Resources',
                'PD + Security', 'PD + Download', 'PD + Model', 'PD + Company', 'PD + Other', 'FR + App',
                'FR + GUI', 'FR + Contents', 'FR + Pricing', 'FR + Feature/Functionality', 'FR + Improvement',
                'FR + Update/Version', 'FR + Resources', 'FR + Security', 'FR + Download', 'FR + Model',
                'FR + Company', 'FR + Other']
code_metrics = ['NBI', 'NOC', 'NOM', 'IPM', 'CC', 'WMC', 'NOCH', 'DIT', 'LCOM', 'CBO', 'PPIV', 'APD', 'BSMC', 'WKL',
                'LOCL', 'GPS', 'XML', 'NTO', 'NET', 'I/O', 'SQL', 'BMAP']

pd_metrics = [x for x in user_metrics if 'PD' in x]
pd_metrics = [x for x in pd_metrics if 'Other' not in x]
fr_metrics = [x for x in user_metrics if 'FR' in x]
fr_metrics = [x for x in fr_metrics if 'Other' not in x]

pd_rows = ['PD', 'App', 'GUI', 'Content', 'Pricing', 'Feature', 'Improv.', 'Update', 'Res.', 'Sec.', 'Down.', 'Model', 'Company']
fr_rows = ['FR', 'App', 'GUI', 'Content', 'Pricing', 'Feature', 'Improv.', 'Update', 'Res.', 'Sec.', 'Down.', 'Model', 'Company']