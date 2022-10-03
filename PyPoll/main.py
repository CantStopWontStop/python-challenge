import pandas as pd
import os


path = "resources/election_data.csv"

election_data_raw = pd.read_csv(path)

election_results = election_data_raw.groupby("Candidate").agg(
    Votes = ('Ballot ID','count')
)

election_results['Prcent'] = election_results['Votes']/len(election_data_raw) * 100


winner = election_results[election_results['Votes'] == election_results['Votes'].max()]

output_path = os.path.join("analysis", "election_results.txt")

lines = [f'There were {len(election_data_raw):,} ballots cast in this election.', 
f'{election_results}',
f'The winner is {winner.index[0]}.']


with open(output_path, 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
        f.write('\n')

print(f'There were {len(election_data_raw):,} ballots cast in this election.' + "\n" + "\n" +
f'{election_results}' + "\n" + "\n" + f'The winner is {winner.index[0]}.')