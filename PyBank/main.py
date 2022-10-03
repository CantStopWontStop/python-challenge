
import pandas as pd
import os


budget_data = pd.read_csv("resources/budget_data.csv") 



n_months = len(budget_data)

total = budget_data['Profit/Losses'].sum()


budget_data['Lag Value'] = budget_data['Profit/Losses'].shift(1)

budget_data['Change'] =  budget_data['Profit/Losses'] - budget_data['Lag Value']

budget_data.sort_values("Change", ascending = False)


avg_change = budget_data['Change'].mean()



max_change = budget_data[budget_data['Change'] == budget_data['Change'].max()]


min_change = budget_data[budget_data['Change'] == budget_data['Change'].min()]


pd.options.display.float_format = '{:, .2f}'.format


output_path = os.path.join("analysis", "financial_analysis.txt")

lines = [f'Total Months: {n_months}', 
f'Total: ${total}',
f'Average Change: {avg_change}',
f'Average Change: {avg_change}',
f'Greatest Increase in Profits: {max_change["Date"].loc[max_change.index[0]]} (${max_change["Change"].loc[max_change.index[0]]})',
f'Greatest Decrease in Profits: {min_change["Date"].loc[min_change.index[0]]} (${min_change["Change"].loc[min_change.index[0]]})']


with open(output_path, 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
        
        
print(f'Total Months: {n_months}')
print(f'Total: ${total}')
print(f'Average Change: {avg_change}')
print(f'Greatest Increase in Profits: {max_change["Date"].loc[max_change.index[0]]} (${max_change["Change"].loc[max_change.index[0]]})')
print(f'Greatest Decrease in Profits: {min_change["Date"].loc[min_change.index[0]]} (${min_change["Change"].loc[min_change.index[0]]})')

