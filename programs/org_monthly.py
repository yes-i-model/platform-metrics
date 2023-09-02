import pandas as pd

def get_valid_filename(prompt):
    while True:
        try:
            filename = input(prompt)
            if not filename.endswith(".csv"):
                filename += ".csv"
            with open(filename, "r"):
                pass
            return filename
        except FileNotFoundError:
            print("File not found, try again.")

data = get_valid_filename("OMG Pendo File: ")
cs_initiatives = get_valid_filename("CS Initiatives File: ")
initiative_download = get_valid_filename("Initiative Downloads: ")
initiative_explore = get_valid_filename("Initiative Exploration: ")

data = pd.read_csv(data)
dwn = pd.read_csv(initiative_download)
csin = pd.read_csv(cs_initiatives)
initexp = pd.read_csv(initiative_explore)

data.loc[:, "Org"] = data["email"].str.extract(r'(?<=\@)(.[^.]*)', expand=False)
init_launch_power = data.sort_values(by='Clicks for Measure: Initiative: Setup - Launch Initiative', ascending=False)
init_open_power = data.sort_values(by='Clicks for Measure: Initiatives - Initiative | Open', ascending=False)
plan_launch_power = data.sort_values(by='Clicks for Plan: New Plan - Run Plan', ascending=False)
plan_open_power = data.sort_values(by='Clicks for Plan: Plans - Plan | Open', ascending=False)
buy_run_power = data.sort_values(by='Clicks for Buy: Plan Setup: Create Plan', ascending=False)
buy_open_power = data.sort_values(by='Clicks for Buy: Investment Plans - Plan | Open', ascending=False)
audience_run_power = data.sort_values(by='Clicks for Audiences: New Audience - Create Audience', ascending=False)
audience_open_power = data.sort_values(by='Clicks for Audiences: Audiences - Audience | Open', ascending=False)
users = data['Visitor ID'].shape[0]
active = data[data['Days Active'] >= 3].shape[0]
active_ds = data[data['Days Active'] >= 3]
nonactive_ds = data[data['Days Active'] < 3]
top15 = data[data['Time on Site (minutes)'] <= 15].shape[0]
top30 = data[data['Time on Site (minutes)'].between(16,30)].shape[0]
top60 = data[data['Time on Site (minutes)'].between(31,60)].shape[0]
top90 = data[data['Time on Site (minutes)'].between(61,90)].shape[0]
top120 = data[data['Time on Site (minutes)'].between(91,120)].shape[0]
top150 = data[data['Time on Site (minutes)'].between(121,150)].shape[0]
top180 = data[data['Time on Site (minutes)'].between(151,180)].shape[0]
top181plus = data[data['Time on Site (minutes)'] > 180].shape[0]
exp5 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(1,5)].shape[0]
exp10 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(6,10)].shape[0]
exp15 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(11,15)].shape[0]
exp20 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(61,90)].shape[0]
exp30 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(91,120)].shape[0]
exp40 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(121,150)].shape[0]
exp50 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(151,180)].shape[0]
exp60 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(151,180)].shape[0]
exp61plus = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'] > 180].shape[0]
measure_users = data[data['Days Active for Measure: BUCKET'] > 0]
measure_actives = data[data['Days Active for Measure: BUCKET'] >= 3]
measure_nonactives = data[data['Days Active for Measure: BUCKET'].between(1,3)]
plan_users = data[data['Days Active for Plan: BUCKET'] > 0]
plan_actives = data[data['Days Active for Plan: BUCKET'] >= 3]
plan_nonactives = data[data['Days Active for Plan: BUCKET'].between(1,3)]
buy_users = data[data['Days Active for Buy: BUCKET'] > 0]
buy_actives = data[data['Days Active for Buy: BUCKET'] >= 3]
buy_nonactives = data[data['Days Active for Buy: BUCKET'].between(1,3)]
audience_users = data[data['Days Active for Audiences: BUCKET'] > 0]
audience_actives = data[data['Days Active for Audiences: BUCKET'] >= 3]
audience_nonactives = data[data['Days Active for Audiences: BUCKET'].between(1,3)]
allocate_users = data[data['Days Active for Allocate: BUCKET'] > 0]
allocate_actives = data[data['Days Active for Allocate: BUCKET'] >= 3]
allocate_nonactives = data[data['Days Active for Allocate: BUCKET'].between(1,3)]
download_cols = dwn.columns[dwn.columns.str.startswith('Clicks')]
total_downloads = dwn[download_cols].values.sum()
downloaded_users = dwn.loc[dwn[download_cols].sum(axis=1) > 0, 'Visitor ID'].unique()
num_unique_users = len(downloaded_users)
init_launch5 = data[data['Clicks for Measure: Initiative: Setup - Launch Initiative'] >= 5].shape[0]
init_open10 = data[data['Clicks for Measure: Initiatives - Initiative | Open'] >= 10].shape[0]
plan_run5 = data[data['Clicks for Plan: New Plan - Run Plan'] >= 5].shape[0]
plan_open15 = data[data['Clicks for Plan: Plans - Plan | Open'] >= 15].shape[0]
buy_run5 = data[data['Clicks for Buy: Plan Setup: Create Plan'] >= 5].shape[0]
buy_open10 = data[data['Clicks for Buy: Investment Plans - Plan | Open'] >= 10].shape[0]
audience_run5 = data[data['Clicks for Audiences: New Audience - Create Audience'] >= 5].shape[0]
audience_open10 = data[data['Clicks for Audiences: Audiences - Audience | Open'] >= 10].shape[0]

print('Total OMG Users:  ' + str(users))
print('Total OMG Active Users:  ' + str(active))
print('Avg. Time Spent on Platform:  ' + str(round(data['Time on Site (minutes)'].mean(), 2)))
print('Avg. Days Spent on Platform:  ' + str(round(data['Days Active'].mean(), 2)))
print(' ')
print('Avg. NON ACTIVE Time Spent on Platform:  ' + str(round(nonactive_ds['Time on Site (minutes)'].mean(), 2)))
print('Avg. ACTIVE Time Spent on Platform:  ' + str(round(active_ds['Time on Site (minutes)'].mean(), 2)))
print('Avg. NON ACTIVE Days Spent on Platform:  ' + str(round(nonactive_ds['Days Active'].mean(), 2)))
print('Avg. ACTIVE Days Spent on Platform:  ' + str(round(active_ds['Days Active'].mean(), 2)))
print(' ')
print('Total Initiatives Launched:  ' + str(data['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Total Plans Run:  ' + str(data['Clicks for Plan: New Plan - Run Plan'].sum()))
print('Total Audi)ences Saved:  ' + str(data['Clicks for Audiences: New Audience - Create Audience'].sum()))
print(' ')
print("ToP 0-15: " + str(top15))
print("ToP 16-30: " + str(top30))
print("ToP 31-60: " + str(top60))
print("ToP 61-90: " + str(top90))
print("ToP 91-120: " + str(top120))
print("ToP 121-150: " + str(top150))
print("ToP 151-180: " + str(top180))
print("ToP 181+: " + str(top181plus))
print(' ')
print('Hearts & Science Actives: ' + str(active_ds[active_ds['Org'] == 'hearts-science'].shape[0]))
print('Hearts & Science Non-Actives: ' + str(nonactive_ds[nonactive_ds['Org'] == 'hearts-science'].shape[0]))
print('OMD Actives: ' + str(active_ds[active_ds['Org'] == 'omd'].shape[0]))
print('OMD Non-Actives: ' + str(nonactive_ds[nonactive_ds['Org'] == 'omd'].shape[0]))
print('PHD Actives: ' + str(active_ds[active_ds['Org'] == 'phdmedia'].shape[0]))
print('PHD Non-Actives: ' + str(nonactive_ds[nonactive_ds['Org'] == 'phdmedia'].shape[0]))
print('Annalect Actives: ' + str(active_ds[active_ds['Org'] == 'annalect'].shape[0]))
print('Annalect Non-Actives: ' + str(nonactive_ds[nonactive_ds['Org'] == 'annalect'].shape[0]))
print('Resolution Actives: ' + str(active_ds[active_ds['Org'] == 'resolution'].shape[0]))
print('Resolution Non-Actives: ' + str(nonactive_ds[nonactive_ds['Org'] == 'resolution'].shape[0]))
print('OMG Actives: ' + str(active_ds[active_ds['Org'].isin(['omnicommediagroup', 'omg23'])].shape[0]))
print('OMG Non-Actives: ' + str(nonactive_ds[nonactive_ds['Org'].isin(['omnicommediagroup', 'omg23'])].shape[0]))
print(' ')
print('MEASURE APP USAGE')
print('----------------------------')
print('Total Measure Users:  ' + str(measure_users.shape[0]))
print('Total Measure Active Users:  ' + str(measure_actives.shape[0]))
print('Avg. Time Spent on Measure:  ' + str(round(measure_users['Time On Page (minutes) for Measure: BUCKET'].mean(), 2)))
print('Avg. Days Spent on Measure:  ' + str(round(measure_users['Days Active for Measure: BUCKET'].mean(), 2)))
print(' ')
print('Avg. NON ACTIVE Time Spent on Measure:  ' + str(round(measure_nonactives['Time On Page (minutes) for Measure: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Time Spent on Measure:  ' + str(round(measure_actives['Time On Page (minutes) for Measure: BUCKET'].mean(), 2)))
print('Avg. NON ACTIVE Days Spent on Measure:  ' + str(round(measure_nonactives['Days Active for Measure: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Days Spent on Measure:  ' + str(round(measure_actives['Days Active for Measure: BUCKET'].mean(), 2)))
print(' ')
print('Total Initiatives Launched:  ' + str(data['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Total Initiatives Opened:  ' + str(data['Clicks for Measure: Initiatives - Initiative | Open'].sum()))
print(f'Total CSV downloads: {total_downloads} - Users: {num_unique_users}')
print('Total CS Initiatives: ' + str(csin.loc[csin["holdingCompanyName"] == 'Omnicom Media Group', 'Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print(' ')
print("Texp 0-5: " + str(exp5))
print("Texp 6-10: " + str(exp10))
print("Texp 11-15: " + str(exp15))
print("Texp 16-20: " + str(exp20))
print("Texp 21-30: " + str(exp30))
print("Texp 31-40: " + str(exp40))
print("Texp 41-50: " + str(exp50))
print("Texp 51-60: " + str(exp60))
print("Texp 61+: " + str(exp61plus))
print(" ")
print('Initiative Exploration – Average vs. Median Page Views: ')
print('---------------------------------')
print('USERS')
print('---------------------------------')
print('Overview: ' + str(initexp[initexp['Page Views for Measure: Initiative: Overview'] > 0].shape[0]))
print('Audience Composition: ' + str(initexp[initexp['Page Views for Measure: Initiative: Audience Insights: Audience Composition'] > 0].shape[0]))
print('Detail: ' + str(initexp[initexp['Page Views for Measure: Initiative: Performance: Detail'] > 0].shape[0]))
print('Conversion: ' + str(initexp[initexp['Page Views for Measure: Initiative: Performance: Conversion'] > 0].shape[0]))
print('Frequency: ' + str(initexp[initexp['Page Views for Measure: Initiative: Performance: Frequency'] > 0].shape[0]))
print('Overlap: ' + str(initexp[initexp['Page Views for Measure: Initiative: Performance: Overlap'] > 0].shape[0]))
print('Competitor Overview: ' + str(initexp[initexp['Page Views for Measure: Initiative: Competitive Insights: Competitor Overview'] > 0].shape[0]))
print('Optimization Segments: ' + str(initexp[initexp['Page Views for Measure: Initiative: Optimization: Optimization Segments'] > 0].shape[0]))
print('Scenarios: ' + str(initexp[initexp['Page Views for Measure: Initiative: Optimization: Scenarios'] > 0].shape[0]))
print('Recommendations: ' + str(initexp[initexp['Page Views for Measure: Initiative: Optimization: Recommendations'] > 0].shape[0]))
print(' ')
print('AVERAGE PAGE VIEWS')
print('---------------------------------')
print('Overview: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Overview'] > 0, 'Page Views for Measure: Initiative: Overview'].mean(), 2)))
print('Audience Composition: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Audience Insights: Audience Composition'] > 0, 'Page Views for Measure: Initiative: Audience Insights: Audience Composition'].mean(), 2)))
print('Detail: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Detail'] > 0, 'Page Views for Measure: Initiative: Performance: Detail'].mean(), 2)))
print('Conversion: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Conversion'] > 0, 'Page Views for Measure: Initiative: Performance: Conversion'].mean(), 2)))
print('Frequency: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Frequency'] > 0, 'Page Views for Measure: Initiative: Performance: Frequency'].mean(), 2)))
print('Overlap: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Overlap'] > 0, 'Page Views for Measure: Initiative: Performance: Overlap'].mean(), 2)))
print('Competitor Overview: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Competitive Insights: Competitor Overview'] > 0, 'Page Views for Measure: Initiative: Competitive Insights: Competitor Overview'].mean(), 2)))
print('Optimization Segments: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Optimization: Optimization Segments'] > 0, 'Page Views for Measure: Initiative: Optimization: Optimization Segments'].mean(), 2)))
print('Scenarios: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Optimization: Scenarios'] > 0, 'Page Views for Measure: Initiative: Optimization: Scenarios'].mean(), 2)))
print('Recommendations: ' + str(round(initexp.loc[initexp['Page Views for Measure: Initiative: Optimization: Recommendations'] > 0, 'Page Views for Measure: Initiative: Optimization: Recommendations'].mean(), 2)))
print(' ')
print('MEDIAN PAGE VIEWS')
print('---------------------------------')
print('Overview: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Overview'] > 0, 'Page Views for Measure: Initiative: Overview'].median()))
print('Audience Composition: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Audience Insights: Audience Composition'] > 0, 'Page Views for Measure: Initiative: Audience Insights: Audience Composition'].median()))
print('Detail: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Detail'] > 0, 'Page Views for Measure: Initiative: Performance: Detail'].median()))
print('Conversion: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Conversion'] > 0, 'Page Views for Measure: Initiative: Performance: Conversion'].median()))
print('Frequency: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Frequency'] > 0, 'Page Views for Measure: Initiative: Performance: Frequency'].median()))
print('Overlap: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Performance: Overlap'] > 0, 'Page Views for Measure: Initiative: Performance: Overlap'].median()))
print('Competitor Overview: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Competitive Insights: Competitor Overview'] > 0, 'Page Views for Measure: Initiative: Competitive Insights: Competitor Overview'].median()))
print('Optimization Segments: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Optimization: Optimization Segments'] > 0, 'Page Views for Measure: Initiative: Optimization: Optimization Segments'].median()))
print('Scenarios: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Optimization: Scenarios'] > 0, 'Page Views for Measure: Initiative: Optimization: Scenarios'].median()))
print('Recommendations: ' + str(initexp.loc[initexp['Page Views for Measure: Initiative: Optimization: Recommendations'] > 0, 'Page Views for Measure: Initiative: Optimization: Recommendations'].median()))
print(' ')
print('AVERAGE TIME EXPLORING')
print('---------------------------------')
print('Overview: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Overview'] > 0, 'Time On Page (minutes) for Measure: Initiative: Overview'].mean(), 2)))
print('Audience Composition: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Audience Insights: Audience Composition'] > 0, 'Time On Page (minutes) for Measure: Initiative: Audience Insights: Audience Composition'].mean(), 2)))
print('Detail: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Detail'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Detail'].mean(), 2)))
print('Conversion: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Conversion'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Conversion'].mean(), 2)))
print('Frequency: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Frequency'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Frequency'].mean(), 2)))
print('Overlap: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Overlap'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Overlap'].mean(), 2)))
print('Competitor Overview: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Competitive Insights: Competitor Overview'] > 0, 'Time On Page (minutes) for Measure: Initiative: Competitive Insights: Competitor Overview'].mean(), 2)))
print('Optimization Segments: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Optimization: Optimization Segments'] > 0, 'Time On Page (minutes) for Measure: Initiative: Optimization: Optimization Segments'].mean(), 2)))
print('Scenarios: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Optimization: Scenarios'] > 0, 'Time On Page (minutes) for Measure: Initiative: Optimization: Scenarios'].mean(), 2)))
print('Recommendations: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Optimization: Recommendations'] > 0, 'Time On Page (minutes) for Measure: Initiative: Optimization: Recommendations'].mean(),2)))
print(' ')
print('MEDIAN TIME EXPLORING')
print('---------------------------------')
print('Overview: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Overview'] > 0, 'Time On Page (minutes) for Measure: Initiative: Overview'].median(), 2)))
print('Audience Composition: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Audience Insights: Audience Composition'] > 0, 'Time On Page (minutes) for Measure: Initiative: Audience Insights: Audience Composition'].median(), 2)))
print('Detail: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Detail'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Detail'].median(), 2)))
print('Conversion: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Conversion'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Conversion'].median(), 2)))
print('Frequency: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Frequency'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Frequency'].median(), 2)))
print('Overlap: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Performance: Overlap'] > 0, 'Time On Page (minutes) for Measure: Initiative: Performance: Overlap'].median(), 2)))
print('Competitor Overview: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Competitive Insights: Competitor Overview'] > 0, 'Time On Page (minutes) for Measure: Initiative: Competitive Insights: Competitor Overview'].median(), 2)))
print('Optimization Segments: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Optimization: Optimization Segments'] > 0, 'Time On Page (minutes) for Measure: Initiative: Optimization: Optimization Segments'].median(), 2)))
print('Scenarios: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Optimization: Scenarios'] > 0, 'Time On Page (minutes) for Measure: Initiative: Optimization: Scenarios'].median(), 2)))
print('Recommendations: ' + str(round(initexp.loc[initexp['Time On Page (minutes) for Measure: Initiative: Optimization: Recommendations'] > 0, 'Time On Page (minutes) for Measure: Initiative: Optimization: Recommendations'].median(),2)))
print(' ')
print(' ')
print('MEASURE POWER USERS')
print('---------------------------------')
for i in range(init_launch5):
    fname = init_launch_power.iloc[i]['firstName']
    lname = init_launch_power.iloc[i]['lastName']
    company = init_launch_power.iloc[i]['Org']
    init_created = init_launch_power.iloc[i]['Clicks for Measure: Initiatives  - Create Initiative']
    init_launched = init_launch_power.iloc[i]['Clicks for Measure: Initiative: Setup - Launch Initiative']
    init_opened = init_launch_power.iloc[i]['Clicks for Measure: Initiatives - Initiative | Open']
    time_spent = init_launch_power.iloc[i]['Time On Page (minutes) for Measure: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {init_launched} - Opened: {init_opened} - {hours} hours {minutes} minutes')
## Currently allows for duplicates, can be made more efficient
for i in range(init_open10):
    fname = init_open_power.iloc[i]['firstName']
    lname = init_open_power.iloc[i]['lastName']
    company = init_open_power.iloc[i]['Org']
    init_created = init_open_power.iloc[i]['Clicks for Measure: Initiatives  - Create Initiative']
    init_launched = init_open_power.iloc[i]['Clicks for Measure: Initiative: Setup - Launch Initiative']
    init_opened = init_open_power.iloc[i]['Clicks for Measure: Initiatives - Initiative | Open']
    time_spent = init_open_power.iloc[i]['Time On Page (minutes) for Measure: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {init_launched} - Opened: {init_opened} - {hours} hours {minutes} minutes')
print(' ')
print('PLAN APP USAGE')
print('----------------------------')
print('Total Plan Users:  ' + str(plan_users.shape[0]))
print('Total Plan Active Users:  ' + str(plan_actives.shape[0]))
print('Avg. Time Spent on Plan:  ' + str(round(plan_users['Time On Page (minutes) for Plan: BUCKET'].mean(), 2)))
print('Avg. Days Spent on Plan:  ' + str(round(plan_users['Days Active for Plan: BUCKET'].mean(), 2)))
print(' ')
print('Avg. NON ACTIVE Time Spent on Plan:  ' + str(round(plan_nonactives['Time On Page (minutes) for Plan: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Time Spent on Plan:  ' + str(round(plan_actives['Time On Page (minutes) for Plan: BUCKET'].mean(), 2)))
print('Avg. NON ACTIVE Days Spent on Plan:  ' + str(round(plan_nonactives['Days Active for Plan: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Days Spent on Plan:  ' + str(round(plan_actives['Days Active for Plan: BUCKET'].mean(), 2)))
print(' ')
print('Run Plans: ' + str(plan_users['Clicks for Plan: New Plan - Run Plan'].sum())) 
print('Explored Plans: ' + str(plan_users['Clicks for Plan: Plans - Plan | Open'].sum()))
print('Linear Buys: ' + str(plan_users['Clicks for Plan: Plan: Linear Buy - Run Linear Buy'].sum()))
print('Aggregate Buys: ' + str(plan_users['Clicks for Plan: New Aggregate Buy - Run Aggregate Buy'].sum()))
print(' ')
print('Linear Plan POWER USERS')
print('---------------------------------')
for i in range(plan_run5):
    fname = plan_launch_power.iloc[i]['firstName']
    lname = plan_launch_power.iloc[i]['lastName']
    company = plan_launch_power.iloc[i]['Org']
    plan_created = plan_launch_power.iloc[i]['Clicks for Plan - Create Plan']
    plan_launched = plan_launch_power.iloc[i]['Clicks for Plan: New Plan - Run Plan']
    plan_opened = plan_launch_power.iloc[i]['Clicks for Plan: Plans - Plan | Open']
    time_spent = plan_launch_power.iloc[i]['Time On Page (minutes) for Plan: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {plan_launched} - Opened: {plan_opened} - {hours} hours {minutes} minutes')
## Currently allows for duplicates, can be made more efficient
for i in range(plan_open15):
    fname = plan_open_power.iloc[i]['firstName']
    lname = plan_open_power.iloc[i]['lastName']
    company = plan_open_power.iloc[i]['Org']
    plan_created = plan_open_power.iloc[i]['Clicks for Plan - Create Plan']
    plan_launched = plan_open_power.iloc[i]['Clicks for Plan: New Plan - Run Plan']
    plan_opened = plan_open_power.iloc[i]['Clicks for Plan: Plans - Plan | Open']
    time_spent = plan_open_power.iloc[i]['Time On Page (minutes) for Plan: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {plan_launched} - Opened: {plan_opened} - {hours} hours {minutes} minutes')
print(' ')
print('BUY APP USAGE')
print('----------------------------')
print('Total Buy Users:  ' + str(buy_users.shape[0]))
print('Total Buy Active Users:  ' + str(buy_actives.shape[0]))
print('Avg. Time Spent on Buy:  ' + str(round(buy_users['Time On Page (minutes) for Buy: BUCKET'].mean(), 2)))
print('Avg. Days Spent on Buy:  ' + str(round(buy_users['Days Active for Buy: BUCKET'].mean(), 2)))
print(' ')
print('Avg. NON ACTIVE Time Spent on Buy:  ' + str(round(buy_nonactives['Time On Page (minutes) for Buy: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Time Spent on Buy:  ' + str(round(buy_actives['Time On Page (minutes) for Buy: BUCKET'].mean(), 2)))
print('Avg. NON ACTIVE Days Spent on Buy:  ' + str(round(buy_nonactives['Days Active for Buy: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Days Spent on Buy:  ' + str(round(buy_actives['Days Active for Buy: BUCKET'].mean(), 2)))
print(' ')
print('Run Buy: ' + str(buy_users['Clicks for Buy: Plan Setup: Create Plan'].sum())) 
print('Explored Buy: ' + str(buy_users['Clicks for Buy: Investment Plans - Plan | Open'].sum()))
print(' ')
print('Buy POWER USERS')
print('---------------------------------')
for i in range(buy_run5):
    fname = buy_run_power.iloc[i]['firstName']
    lname = buy_run_power.iloc[i]['lastName']
    company = buy_run_power.iloc[i]['Org']
    buy_created = buy_run_power.iloc[i]['Clicks for Buy: Create Plan']
    buy_launched = buy_run_power.iloc[i]['Clicks for Buy: Plan Setup: Create Plan']
    buy_opened = buy_run_power.iloc[i]['Clicks for Buy: Investment Plans - Plan | Open']
    time_spent = buy_run_power.iloc[i]['Time On Page (minutes) for Buy: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {buy_launched} - Opened: {buy_opened} - {hours} hours {minutes} minutes')
## Currently allows for duplicates, can be made more efficient
for i in range(buy_open10):
    fname = buy_open_power.iloc[i]['firstName']
    lname = buy_open_power.iloc[i]['lastName']
    company = buy_open_power.iloc[i]['Org']
    buy_created = buy_open_power.iloc[i]['Clicks for Buy: Create Plan']
    buy_launched = buy_open_power.iloc[i]['Clicks for Buy: Plan Setup: Create Plan']
    buy_opened = buy_open_power.iloc[i]['Clicks for Buy: Investment Plans - Plan | Open']
    time_spent = buy_open_power.iloc[i]['Time On Page (minutes) for Buy: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {buy_launched} - Opened: {buy_opened} - {hours} hours {minutes} minutes')
print(' ')
print('AUDIENCE APP USAGE')
print('----------------------------')
print('Total Audiences Users:  ' + str(audience_users.shape[0]))
print('Total Audiences Active Users:  ' + str(audience_actives.shape[0]))
print('Avg. Time Spent on Audiences:  ' + str(round(audience_users['Time On Page (minutes) for Audiences: BUCKET'].mean(), 2)))
print('Avg. Days Spent on Audiences:  ' + str(round(audience_users['Days Active for Audiences: BUCKET'].mean(), 2)))
print(' ')
print('Avg. NON ACTIVE Time Spent on Audiences:  ' + str(round(audience_nonactives['Time On Page (minutes) for Audiences: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Time Spent on Audiences:  ' + str(round(audience_actives['Time On Page (minutes) for Audiences: BUCKET'].mean(), 2)))
print('Avg. NON ACTIVE Days Spent on Audiences:  ' + str(round(audience_nonactives['Days Active for Audiences: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Days Spent on Audiences:  ' + str(round(audience_actives['Days Active for Audiences: BUCKET'].mean(), 2)))
print(' ')
print('Run Audiences: ' + str(audience_users['Clicks for Audiences: New Audience - Create Audience'].sum())) 
print('Explored Audiences: ' + str(audience_users['Clicks for Audiences: Audiences - Audience | Open'].sum()))
print('TV Viewership Segments: ' + str(audience_users['Clicks for Audiences: New TV Segment - Create Segment'].sum()))
print(' ')
for i in range(audience_run5):
    fname = audience_run_power.iloc[i]['firstName']
    lname = audience_run_power.iloc[i]['lastName']
    company = audience_run_power.iloc[i]['Org']
    tvviewer_created = audience_run_power.iloc[i]['Clicks for Audiences: New TV Segment - Create Segment']
    audience_launched = audience_run_power.iloc[i]['Clicks for Audiences: New Audience - Create Audience']
    audience_opened = audience_run_power.iloc[i]['Clicks for Audiences: Audiences - Audience | Open']
    time_spent = audience_run_power.iloc[i]['Time On Page (minutes) for Audiences: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {audience_launched} - Opened: {audience_opened} - TV Viewership: {tvviewer_created} - {hours} hours {minutes} minutes')
## Currently allows for duplicates, can be made more efficient
for i in range(audience_open10):
    fname = audience_open_power.iloc[i]['firstName']
    lname = audience_open_power.iloc[i]['lastName']
    company = audience_open_power.iloc[i]['Org']
    tvviewer_created = audience_open_power.iloc[i]['Clicks for Audiences: New TV Segment - Create Segment']
    audience_launched = audience_open_power.iloc[i]['Clicks for Audiences: New Audience - Create Audience']
    audience_opened = audience_open_power.iloc[i]['Clicks for Audiences: Audiences - Audience | Open']
    time_spent = audience_open_power.iloc[i]['Time On Page (minutes) for Audiences: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Launched: {audience_launched} - Opened: {audience_opened} - TV Viewership: {tvviewer_created} - {hours} hours {minutes} minutes')
    
print(' ')
print('Allocate APP USAGE')
print('----------------------------')
print('Total Allocate Users:  ' + str(allocate_users.shape[0]))
print('Total Allocate Active Users:  ' + str(allocate_actives.shape[0]))
print('Avg. Time Spent on Allocate:  ' + str(round(allocate_users['Time On Page (minutes) for Allocate: BUCKET'].mean(), 2)))
print('Avg. Days Spent on Allocate:  ' + str(round(allocate_users['Days Active for Allocate: BUCKET'].mean(), 2)))
print(' ')
print('Avg. NON ACTIVE Time Spent on Allocate:  ' + str(round(allocate_nonactives['Time On Page (minutes) for Allocate: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Time Spent on Allocate:  ' + str(round(allocate_actives['Time On Page (minutes) for Allocate: BUCKET'].mean(), 2)))
print('Avg. NON ACTIVE Days Spent on Allocate:  ' + str(round(allocate_nonactives['Days Active for Allocate: BUCKET'].mean(), 2)))
print('Avg. ACTIVE Days Spent on Allocate:  ' + str(round(allocate_actives['Days Active for Allocate: BUCKET'].mean(), 2)))
print(' ')
print('Run Allocate: ' + str(allocate_users['Clicks for Allocate: New Allocation - Run Allocation'].sum())) 
print('Explored Allocate: ' + str(allocate_users['Clicks for Allocate: Allocations - Allocation | Open'].sum()))
print('Submit to Mediaocean: ' + str(allocate_users['Clicks for Allocate: Allocation - Submit to Mediaocean'].sum()))