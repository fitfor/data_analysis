import sys

import pandas as pd


####
# Global Var
ass_rules_path = 'data/ass_rules_v1.pkl'

####
# read data
ass_rules = pd.read_pickle(ass_rules_path)

####
# read sys arguments
activities = []
for ct in range(1, 9):
    activities.append(sys.argv[ct])


####
# define necessary methods
def get_recommendation(activities: list):
    activities = set(activities)
    query_get_matches = ass_rules['antecedents'].apply(lambda ant: set(ant).issubset(activities))
    query_remove_neg_lev = ass_rules['leverage'] <= 0

    ass_rules_queried = ass_rules[query_get_matches]
    ass_rules_queried = ass_rules[query_remove_neg_lev]

    ass_rules_queried = ass_rules_queried.sort_values(by='confidence', ascending=False)
    ass_rules_queried = ass_rules_queried.reset_index(drop=True)

    ass_rules_queried = ass_rules_queried.loc[:4, ['consequents', 'confidence']]

    query_duplicates = (ass_rules_queried['consequents'].duplicated() == False)
    ass_rules_queried = ass_rules_queried[query_duplicates]

    ass_rules_queried['consequents'] = ass_rules_queried['consequents'].apply(lambda x: list(x)[0])
    return (ass_rules_queried)


####
# return recomms
ass_rules = get_recommendation(activities)

{
    'consequent': ass_rules['consequents'].to_list(),
    'confidence': ass_rules['confidence'].to_list()
}

