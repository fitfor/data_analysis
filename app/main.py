import sys

import pandas as pd

from flask import Flask
from flask import jsonify
from flask import request

####
# Global Var
ass_rules_path = 'ass_rules_v1.pkl'


####
# read data
ass_rules = pd.read_pickle(ass_rules_path)


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


app = Flask(__name__)

@app.route('/get-recomm/', methods=['GET', 'POST'])
def get_recomms():
    act1 = request.args.get('act1')
    act2 = request.args.get('act2')
    act3 = request.args.get('act3')

    recoms = get_recommendation([act1, act2, act3])
    recoms = {
        'consequent': recoms['consequents'].to_list(),
        'confidence': recoms['confidence'].to_list()
        }

    return jsonify(recoms)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)