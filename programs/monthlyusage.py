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

data = get_valid_filename("External Usage Pendo File: ")
cs_initiatives = get_valid_filename("CS Initiatives File: ")
elsy_main = get_valid_filename("Elsy External Usage: ")
elsy_reports = get_valid_filename("Elsy Report Usage: ")
initiative_creation = get_valid_filename("Initiative Creation: ")
initiative_download = get_valid_filename("Initiative Downloads: ")
initiative_explore = get_valid_filename("Initiative Exploration: ")
plan_explore = get_valid_filename("Plan Exploration: ")
tableau = get_valid_filename("Tableau: ")

month_yr = data[0:6]

tvm_list = [4719, 904, 4723, 3929, 4714, 4717, 5656, 5392, 4724, 4495, 4715, 3599, 4348, 5653, 5665, 5655, 4713, 4712,
       4720, 5661, 4337, 5652, 4721, 3015, 5666, 5654, 3930, 5663, 5658, 902, 3600, 5657, 4718, 5664, 5660, 5662,
       4722, 3217, 3775, 3777, 5659, 3155, 4716, 3598, 5183, 5163, 6151, 5179, 6194, 6193, 5176, 5191, 5190, 5184,
       6197, 5165, 5171, 5166, 5185, 5162, 5173, 5187, 5181, 6199, 3955, 2856, 5131, 5158, 2855, 5157, 5178, 5164,
       5170, 5186, 5159, 5189, 5174, 5175, 5172, 5127, 5895, 5177, 5129, 5132, 5180, 5854, 5182, 5160, 5850, 6198,
       5169, 5168, 5133, 5167, 5161, 5188, 5128, 5715, 5716, 5717, 5718, 5719, 5720, 5721, 5762]

am_list = [3489, 2736, 2737, 230, 3473, 217, 3490, 229, 3481, 215, 3477, 216, 3491, 220, 224, 233, 2735, 219, 2968, 1143,
      3476, 222, 2748, 3483, 4134, 236, 3482, 517, 213, 2733, 3487, 214, 2967, 234, 2969, 3488, 235, 232, 3486, 2734,
      231, 3484, 3485, 3475, 3641, 3602, 3645, 1894, 269, 3642, 3644, 268, 2701, 1896, 4378, 3643, 4018, 2462, 5603,
      4264, 3278, 3365, 4782, 1898, 847, 4379, 3366, 3367, 3370, 1899, 271, 3639, 945, 1893, 3368, 272, 3640, 1739,
      4311, 3369, 267, 1895, 3638, 5501, 458, 5315, 5393, 1031, 2454, 6217, 3347, 5263, 1238, 78, 2679, 566, 2670, 568,
      4277, 2667, 607, 608, 2281, 2680, 2678, 2673, 2677, 2672, 2665, 575, 2662, 2666, 998, 604, 2671, 881, 2669, 2069,
      610, 2664, 2512, 2259, 2674, 2659, 2843, 2810, 4418, 602, 569, 570, 3523, 1770, 3987, 642, 6397, 6362, 4015, 3979,
      6125, 1768, 5838, 4670, 3989, 3222, 2207, 5793, 4402, 2258, 4188, 5794, 5800, 5618, 6100, 4189, 6101, 4187, 2209,
      5617, 4192, 4400, 4403, 4401, 2340, 2338, 5100, 4528, 4099, 5123, 4100, 3161, 4101, 4405, 4098, 3306, 4286, 4529,
      3159, 4530, 4404, 3163, 4290, 6210, 6221, 6213, 6216, 6215, 6212, 6214, 4005, 6211, 6241, 6369, 6259, 6258, 6269,
      6279, 6264, 6271, 6261, 6277, 6272, 6266, 6267, 6260, 6257, 6275, 6268, 6273, 6262, 6278, 6263, 6274, 6276, 6270,
      6265, 4147, 4150, 4157, 4151, 4155, 4161, 4156, 6254, 4159, 4149, 6253, 4162, 4146, 4152, 4148, 4084, 4145, 6255, 4154,
      5446, 3758, 2723, 4498, 4502, 4497, 3834, 3246, 3322, 3245, 3618, 3320, 3321, 3247, 3323, 3617, 4689, 3783, 3865,
      4421, 3291, 4438, 4441, 5021, 4423, 3286, 4675, 4270, 4781, 4422, 4442, 6112, 3283, 4407, 6113, 3282, 3289, 3290,
      4440, 5503, 3784, 3288, 6406, 3292, 4794, 4443, 3284, 5081, 4439, 4542, 4269, 4875, 3287, 3285, 6381, 3785, 3592,
      3633, 4541, 4795, 5630, 6380, 6111, 3725, 3728, 3746, 5673, 5674, 5671, 5676, 3726, 5677, 3727, 5672, 5675, 5291,
      5294, 5293, 5296, 5292, 4356, 4745, 4358, 4361, 4837, 4836, 4677, 4360, 4834, 4838, 4835, 4357, 4359, 4833, 4678,
      4967, 4459, 5213, 5211, 4385, 4462, 4458, 4384, 4461, 5212, 4460, 4382, 6410, 5280, 4457, 4383, 4456, 4966, 4380,
      5214, 4381, 5279, 4548, 6291, 4665, 4551, 4550, 4549, 5237, 5233, 6447, 5231, 6355, 5232, 5238, 5239, 5236, 5234,
      5235, 5619, 5623, 5628, 5621, 6357, 5620, 501, 635, 5622, 5835, 5829, 5830, 5834, 5831, 5822, 5828, 5833, 5826, 5821,
      5823, 5827, 5832, 5825, 5824]


data = pd.read_csv(data)
tvm = data[data['Visitor ID'].isin(tvm_list)]
am = data[data['Visitor ID'].isin(am_list)]
csin = pd.read_csv(cs_initiatives)
elsydata = pd.read_csv(elsy_main)
elsyrep = pd.read_csv(elsy_reports)
initcrea = pd.read_csv(initiative_creation)
initdwn = pd.read_csv(initiative_download)
initexp = pd.read_csv(initiative_explore)
planexp = pd.read_csv(plan_explore)
tab = pd.read_csv(tableau)

month_year = data[:6]
actives = data[data['Days Active'] >= 3]
active_names = actives.loc[:, ['firstName', 'lastName']]
non_actives = data[data['Days Active'] < 3]
tvmactives = tvm[tvm['Days Active'] >= 3]
tvm_nonactives = tvm[tvm['Days Active'] < 3]
amactives = am[am['Days Active'] >= 3]
am_nonactives = am[am['Days Active'] < 3]
elsy_actives = elsydata[elsydata['Days Active'] >= 3]
elsy_nonactives = elsydata[elsydata['Days Active'] < 3]
toptime = data.sort_values(by='Time on Site (minutes)', ascending=False)
topday = data.sort_values(by='Days Active', ascending=False)
topelsytime = elsydata.sort_values(by='Time on Site (minutes)', ascending=False)
topelsyday = elsydata.sort_values(by='Days Active', ascending=False)
topelsy_po_time = elsyrep.sort_values(by='Time On Page (minutes) for Plan Overview Report: BUCKET', ascending=False)
topelsy_pc_time = elsyrep.sort_values(by='Time On Page (minutes) for Elsy: Plan Comparison Report - BUCKET', ascending=False)
topelsy_cp_time = elsyrep.sort_values(by='Time On Page (minutes) for Elsy: Campaign Performance Report - BUCKET', ascending=False)
topelsy_cm_time = elsyrep.sort_values(by='Time On Page (minutes) for Elsy: Campaign Monitoring Report - BUCKET', ascending=False)
init_launch_power = data.sort_values(by='Clicks for Measure: Initiative: Setup - Launch Initiative', ascending=False)
init_open_power = data.sort_values(by='Clicks for Measure: Initiatives - Initiative | Open', ascending=False)
plan_run_power = data.sort_values(by='Clicks for Plan: New Plan - Run Plan', ascending=False)
plan_open_power = data.sort_values(by='Clicks for Plan: Plans - Plan | Open', ascending=False)
buy_run_power = data.sort_values(by='Clicks for Buy: Plan Setup: Create Plan', ascending=False)
buy_open_power = data.sort_values(by='Clicks for Buy: Investment Plans - Plan | Open', ascending=False)
audience_run_power = data.sort_values(by='Clicks for Audiences: New Audience - Create Audience', ascending=False)
audience_open_power = data.sort_values(by='Clicks for Audiences: Audiences - Audience | Open', ascending=False)
plat15 = data[data['Time on Site (minutes)'].between(1, 15)].shape[0]
plat30 = data[data['Time on Site (minutes)'].between(16, 30)].shape[0]
plat60 = data[data['Time on Site (minutes)'].between(31, 60)].shape[0]
plat90 = data[data['Time on Site (minutes)'].between(61, 90)].shape[0]
plat120 = data[data['Time on Site (minutes)'].between(91, 120)].shape[0]
plat150 = data[data['Time on Site (minutes)'].between(121, 150)].shape[0]
plat180 = data[data['Time on Site (minutes)'].between(151, 180)].shape[0]
plat181_plus = data[data['Time on Site (minutes)'] >= 181].shape[0]

init_expl5 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(1, 5)].shape[0]
init_expl10 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(6, 10)].shape[0]
init_expl15 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(11, 15)].shape[0]
init_expl20 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(16, 20)].shape[0]
init_expl30 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(21, 30)].shape[0]
init_expl40 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(31, 40)].shape[0]
init_expl50 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(41, 50)].shape[0]
init_expl60 = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'].between(51, 60)].shape[0]
init_expl61_plus = initexp[initexp['Time On Page (minutes) for Measure: Initiative EXPLORE BUCKET'] >= 61].shape[0]

plan_expl5 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(1, 5)].shape[0]
plan_expl10 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(6, 10)].shape[0]
plan_expl15 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(11, 15)].shape[0]
plan_expl20 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(16, 20)].shape[0]
plan_expl30 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(21, 30)].shape[0]
plan_expl40 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(31, 40)].shape[0]
plan_expl50 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(41, 50)].shape[0]
plan_expl60 = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'].between(51, 60)].shape[0]
plan_expl61_plus = planexp[planexp['Time On Page (minutes) for Plan: Explore - BUCKET'] >= 61].shape[0]

agency_list = ['Continuum Media', 'CrossMedia Agency', 'MMI', 'Omnicom Media Group', 'GroupM', 'dentsu', 'Publicis Media', 'Horizon Media', 'INNOCEAN', 'Butler/Till', 'Luxottica', 'Empower', 'Safelite', 'SCS', 'Kepler Group', 'ProMedia', 'Haworth', 'Interpublic Group', 'Icon Media Direct', 'Media by Mother', 'The Tombras Group']
brand_list = ['PepsiCo', 'Southern New Hampshire University', 'Squarespace', 'Kimberly-Clark Corp.', 'Angi', 'DoorDash', "Papa John's", 'Chewy', 'Constellation Brands', 'Eli Lilly', 'Leaf Home', 'The Vanguard Group', 'Amazon', 'Vantage']
networks_list = ['Univision', 'NBCU', 'WarnerMedia', 'Discovery', 'Disney']
agency_users = data[data["holdingCompanyName"].isin(agency_list)]
brand_users = data[data["holdingCompanyName"].isin(brand_list)]
network_users = data[data["holdingCompanyName"].isin(networks_list)]
active_agency = agency_users[agency_users['Days Active'] >= 3]
active_brand = brand_users[brand_users['Days Active'] >= 3]
active_network = network_users[network_users['Days Active'] >= 3]
measure = data[data['Time On Page (minutes) for Measure: BUCKET'] > 0]
measure_actives = measure[measure['Days Active for Measure: BUCKET'] >= 3]
measure_nonactives = measure[measure['Days Active for Measure: BUCKET'] < 3]
plan = data[data['Time On Page (minutes) for Plan: BUCKET'] > 0]
plan_actives = plan[plan['Days Active for Plan: BUCKET'] >= 3]
plan_nonactives = plan[plan['Days Active for Plan: BUCKET'] < 3]
buy = data[data['Time On Page (minutes) for Buy: BUCKET'] > 0]
buy_actives = buy[buy['Days Active for Buy: BUCKET'] >= 3]
buy_nonactives = buy[buy['Days Active for Buy: BUCKET'] < 3]
audiences = data[data['Time On Page (minutes) for Audiences: BUCKET'] > 0]
audiences_actives = audiences[audiences['Days Active for Audiences: BUCKET'] >= 3]
audiences_nonactives = audiences[audiences['Days Active for Audiences: BUCKET'] < 3]
allocate = data[data['Time On Page (minutes) for Allocate: BUCKET'] > 0]
allocate_actives = allocate[allocate['Days Active for Allocate: BUCKET'] >= 3]
allocate_nonactives = allocate[allocate['Days Active for Allocate: BUCKET'] < 3]
cs_orgs_init = csin.groupby('holdingCompanyName')['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()
cs_orgs_nozero = cs_orgs_init[cs_orgs_init != 0]
cs_orgs_sorted = cs_orgs_nozero.sort_index()
client_orgs_init = data.groupby('holdingCompanyName')['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()
client_orgs_nozero = client_orgs_init[client_orgs_init != 0]
client_orgs_sorted = client_orgs_nozero.sort_index()
data['Abandoned Initiatives'] = data['Clicks for Measure: Initiatives  - Create Initiative'] - data['Clicks for Measure: Initiative: Setup - Launch Initiative']
top_aban_init = data.sort_values(by='Abandoned Initiatives', ascending=False)
init_launch5 = data[data['Clicks for Measure: Initiative: Setup - Launch Initiative'] >= 5].shape[0]
init_open10 = data[data['Clicks for Measure: Initiatives - Initiative | Open'] >= 10].shape[0]
plan_run5 = data[data['Clicks for Plan: New Plan - Run Plan'] >= 5].shape[0]
plan_open15 = data[data['Clicks for Plan: Plans - Plan | Open'] >= 15].shape[0]
buy_run5 = data[data['Clicks for Buy: Plan Setup: Create Plan'] >= 5].shape[0]
buy_open10 = data[data['Clicks for Buy: Investment Plans - Plan | Open'] >= 10].shape[0]
audience_run5 = data[data['Clicks for Audiences: New Audience - Create Audience'] >= 5].shape[0]
audience_open10 = data[data['Clicks for Audiences: Audiences - Audience | Open'] >= 10].shape[0]

tab_externals = tab[~tab["username"].str.contains("videoamp.com")]
tab_externals = tab_externals[~tab_externals["username"].str.contains("Revenue_Team")]
tab_externals = tab_externals[~tab_externals["username"].str.contains("revenue")]
tab_externals = tab_externals[~tab_externals["username"].str.contains("tstavropoulos")]
tab_externals = tab_externals[~tab_externals["username"].str.contains("elsy")]
tab_externals = tab_externals[~tab_externals["username"].str.contains("video")]
tab_externals = tab_externals[~tab_externals["username"].str.contains("gmail")]
tab_externals["Date"] = tab_externals["Created At"].str.extract(r'(\d+/\d+/\d+)', expand=False)
distinct_tabdates = tab_externals.groupby('username')['Date'].nunique().reset_index()
distinct_tabusers = tab_externals['username'].nunique()
distinct_tabdates = distinct_tabdates.rename(columns={'Date': 'Number of Days Active'})
card = tab_externals[tab_externals['Name (Hist Workbooks)'] == 'CARD']
card_lite = tab_externals[tab_externals['Name (Hist Workbooks)'] == 'CARD Lite']
distinct_carddates = card.groupby('username')['Date'].nunique().reset_index()
distinct_cardusers = card['username'].nunique()
distinct_carddates = distinct_carddates.rename(columns={'Date': 'Number of Days Active'})
card = card.copy()
card.loc[:, "holdCom"] = card["username"].str.extract(r'(?<=\@)(.[^.]*)', expand=False)
card_lite = card_lite.copy()
card_lite.loc[:, "holdCom"] = card_lite["username"].str.extract(r'(?<=\@)(.[^.]*)', expand=False)
distinct_cardlitedates = card_lite.groupby('username')['Date'].nunique().reset_index()
distinct_cardliteusers = card_lite['username'].nunique()
distinct_cardlitedates = distinct_cardlitedates.rename(columns={'Date': 'Number of Days Active'})
card_hc = card.groupby('holdCom')['username'].nunique().reset_index()
card_hc = card_hc.rename(columns={'username': 'num_users', 'holdCom': 'company_name'})
card_litehc = card_lite.groupby('holdCom')['username'].nunique().reset_index()
card_litehc = card_litehc.rename(columns={'username': 'num_users', 'holdCom': 'company_name'})
tab_user_list = tab_externals['username'].tolist()
tabxplat = data[data['email'].isin(tab_user_list)]
card_byapp = card.groupby(['Name (Hist Views)', 'holdCom']).size().reset_index(name='count')
cardlite_byapp = card_lite.groupby(['Name (Hist Views)', 'holdCom']).size().reset_index(name='count')

download = str(input("Would you like to download Active Users? (y/n): ")).lower()
if download in ['y', 'yes']:
    actives.to_csv(f'{month_yr}_actives.csv')
    measure_actives.to_csv(f'{month_yr}_measure_actives.csv')
    plan_actives.to_csv(f'{month_yr}_plan_actives.csv')
    buy_actives.to_csv(f'{month_yr}_buy_actives.csv')
    audiences_actives.to_csv(f'{month_yr}_audiences_actives.csv')
    allocate_actives.to_csv(f'{month_yr}_allocate_actives.csv')    
else:
    pass

print('Total Users in Platform: ' + str(data['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(data[data['Days Active'] >= 3].shape[0]))
print('Average Time on Platform: ' + str(round(data['Time on Site (minutes)'].mean(), 2)))
print('Average Days on Platform: ' + str(round(data['Days Active'].mean(), 2)))
print('Average ACTIVE Time on Platform: ' + str(round(actives['Time on Site (minutes)'].mean(), 2)))
print('Average NON-ACTIVE Time on Platform: ' + str(round(non_actives['Time on Site (minutes)'].mean(), 2)))
print('Average ACTIVE Days on Platform: ' + str(round(actives['Days Active'].mean(), 2)))
print('Average NON-ACTIVE Days on Platform: ' + str(round(non_actives['Days Active'].mean(), 2)))
print(" ")
print('Top 5 Users by Time on Platform: ')
print('---------------------------------')
for i in range(5):
    fname = toptime.iloc[i]['firstName']
    lname = toptime.iloc[i]['lastName']
    company = toptime.iloc[i]['holdingCompanyName']
    time_spent = toptime.iloc[i]['Time on Site (minutes)']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - {hours} hours {minutes} minutes')
    
print(" ")
print('Top 5 Users by Day on Platform: ')
print('---------------------------------')
for i in range(5):
    fname = topday.iloc[i]['firstName']
    lname = topday.iloc[i]['lastName']
    company = topday.iloc[i]['holdingCompanyName']
    days = topday.iloc[i]['Days Active']
    print(f'{fname} {lname} - {company} - {days} days')

print(" ")
print('TVM Pro Actives: ' + str(tvmactives["Visitor ID"].shape[0]))
print('Advanced Measurement Actives: ' + str(amactives["Visitor ID"].shape[0]))
print('Other Actives: ' + str(int(data[data['Days Active'] >= 3].shape[0]) - (int(amactives["Visitor ID"].shape[0]) + int(tvmactives["Visitor ID"].shape[0]))))
print(" ")
print('VideoAmp Platform Usage – Time in the Platform: ')
print('---------------------------------')
print("Time on Platform 0-15: " + str(plat15))
print("Time on Platform 16-30: " + str(plat30))
print("Time on Platform 31-60: " + str(plat60))
print("Time on Platform 61-90: " + str(plat90))
print("Time on Platform 91-120: " + str(plat120))
print("Time on Platform 121-150: " + str(plat150))
print("Time on Platform 151-180: " + str(plat180))
print("Time on Platform 151+:  " + str(plat181_plus))
print(" ")
print('---------------------------------')
print('---------------------------------')
print(" ")
print('ADVANCED MEASUREMENT USERS')
print('---------------------------------')
print('Total Users in Platform: ' + str(am['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(am[am['Days Active'] >= 3].shape[0]))
print('Average Time on Platform: ' + str(round(am['Time on Site (minutes)'].mean(), 2)))
print('Average ACTIVE Time on Platform: ' + str(round(amactives['Time on Site (minutes)'].mean(), 2)))
print('Average NON-ACTIVE Time on Platform: ' + str(round(am_nonactives['Time on Site (minutes)'].mean(), 2)))
print('Average Days on Platform: ' + str(round(am['Days Active'].mean(), 2)))
print('Average ACTIVE Days on Platform: ' + str(round(amactives['Days Active'].mean(), 2)))
print('Average NON-ACTIVE Days on Platform: ' + str(round(am_nonactives['Days Active'].mean(), 2)))
print('Launched Initiatives: ' + str(am['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Abandoned Initiatives: ' + str(am['Clicks for Measure: Initiatives  - Create Initiative'].sum() - am['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Plans Run: ' + str(am['Clicks for Plan: New Plan - Run Plan'].sum()))
print('Abandoned Plans: ' + str(am['Clicks for Plan - Create Plan'].sum() - am['Clicks for Plan: New Plan - Run Plan'].sum()))
print('Audiences Saved: ' + str(am['Clicks for Audiences: New Audience - Create Audience'].sum()))
print('Audiences Abandoned: ' + str(am['Clicks for Audiences: Audiences - Create Audience'].sum() - am['Clicks for Audiences: New Audience - Create Audience'].sum()))
print(" ")
print('TVMPRO USERS')
print('---------------------------------')
print('Total Users in Platform: ' + str(tvm['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(tvm[tvm['Days Active'] >= 3].shape[0]))
print('Average Time on Platform: ' + str(round(tvm['Time on Site (minutes)'].mean(), 2)))
print('Average ACTIVE Time on Platform: ' + str(round(tvmactives['Time on Site (minutes)'].mean(), 2)))
print('Average NON-ACTIVE Time on Platform: ' + str(round(tvm_nonactives['Time on Site (minutes)'].mean(), 2)))
print('Average Days on Platform: ' + str(round(tvm['Days Active'].mean(), 2)))
print('Average ACTIVE Days on Platform: ' + str(round(tvmactives['Days Active'].mean(), 2)))
print('Average NON-ACTIVE Days on Platform: ' + str(round(tvm_nonactives['Days Active'].mean(), 2)))
print('Launched Initiatives: ' + str(tvm['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Abandoned Initiatives: ' + str(tvm['Clicks for Measure: Initiatives  - Create Initiative'].sum() - tvm['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Audiences Saved: ' + str(tvm['Clicks for Audiences: New Audience - Create Audience'].sum()))
print('Audiences Abandoned: ' + str(tvm['Clicks for Audiences: Audiences - Create Audience'].sum() - tvm['Clicks for Audiences: New Audience - Create Audience'].sum()))
print(" ")
print('ORGANIZATION USAGE')
print('---------------------------------')
print('AGENCIES:',agency_users['Visitor ID'].count())
print('BRANDS:',brand_users['Visitor ID'].count())
print('NETWORKS:',network_users['Visitor ID'].count())
print(" ")
print('ACTIVE AGENCIES:',active_agency['Visitor ID'].count())
print('ACTIVE BRANDS:',active_brand['Visitor ID'].count())
print('ACTIVE NETWORKS:',active_network['Visitor ID'].count())
print(" ")
print('MEASURE APP USAGE')
print('---------------------------------')
print('Total Users in Platform: ' + str(measure['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(measure_actives.shape[0]))
print('Average Time on Platform: ' + str(round(measure['Time On Page (minutes) for Measure: BUCKET'].mean(), 2)))
print('Average ACTIVE Time on Platform: ' + str(round(measure_actives['Time On Page (minutes) for Measure: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Time on Platform: ' + str(round(measure_nonactives['Time On Page (minutes) for Measure: BUCKET'].mean(), 2)))
print('Average Days on Platform: ' + str(round(measure['Days Active for Measure: BUCKET'].mean(), 2)))
print('Average ACTIVE Days on Platform: ' + str(round(measure_actives['Days Active for Measure: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Days on Platform: ' + str(round(measure_nonactives['Days Active for Measure: BUCKET'].mean(), 2)))
print(" ")
print('Created Initiatives: ' + str(measure['Clicks for Measure: Initiatives  - Create Initiative'].sum()))
print('Launched Initiatives: ' + str(measure['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print('Explored Initiatives: ' + str(measure['Clicks for Measure: Initiatives - Initiative | Open'].sum()))
print('Average Abandoned Initiatives: ' + str(round((measure['Clicks for Measure: Initiatives  - Create Initiative'].sum() - measure['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()) / measure[measure['Clicks for Measure: Initiatives  - Create Initiative'] > 0].shape[0], 2)))
print('Abandoned Initiatives: ' + str(measure['Clicks for Measure: Initiatives  - Create Initiative'].sum() - measure['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print(" ")
print('INITIATIVE CREATION')
print('---------------------------------')
print('USERS')
print('---------------------------------')
print('Initiative Setup: ' + str(initcrea[initcrea['Time On Page (minutes) for Measure: New Initiative: Initiative Setup'] > 0].shape[0]))
print('Objectives: ' + str(initcrea[initcrea['Time On Page (minutes) for Measure: New Initiative: Objectives'] > 0].shape[0]))
print('Investments: ' + str(initcrea[initcrea['Time On Page (minutes) for Measure: New Initiative: Investments'] > 0].shape[0]))
print('Strategies: ' + str(initcrea[initcrea['Time On Page (minutes) for Measure: New Initiative: Strategies'] > 0].shape[0]))
print('Competitors: ' + str(initcrea[initcrea['Time On Page (minutes) for Measure: New Initiative | Competitors'] > 0].shape[0]))
print(' ')
print('AVERAGES')
print('---------------------------------')
print('Initiative Setup: ' + str(round(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Initiative Setup'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Initiative Setup'].mean(), 2)))
print('Objectives: ' + str(round(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Objectives'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Objectives'].mean(), 2)))
print('Investments: ' + str(round(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Investments'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Investments'].mean(), 2)))
print('Strategies: ' + str(round(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Strategies'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Strategies'].mean(), 2)))
print('Competitors: ' + str(round(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative | Competitors'] > 0, 'Time On Page (minutes) for Measure: New Initiative | Competitors'].mean(), 2)))
print(' ')
print('MEDIAN')
print('---------------------------------')
print('Initiative Setup: ' + str(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Initiative Setup'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Initiative Setup'].median()))
print('Objectives: ' + str(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Objectives'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Objectives'].median()))
print('Investments: ' + str(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Investments'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Investments'].median()))
print('Strategies: ' + str(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative: Strategies'] > 0, 'Time On Page (minutes) for Measure: New Initiative: Strategies'].median()))
print('Competitors: ' + str(initcrea.loc[initcrea['Time On Page (minutes) for Measure: New Initiative | Competitors'] > 0, 'Time On Page (minutes) for Measure: New Initiative | Competitors'].median()))
print(' ')
print('CS Initiatives')
print('---------------------------------')
print('CS Initiatives Launched: ' + str(csin['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print(cs_orgs_sorted)
print(' ')
print('Client Initiatives Launched: ')
print(client_orgs_sorted)
print(' ')
print('Abandoned Initiatives')
print('---------------------------------')
for i in range(10):
    fname = top_aban_init.iloc[i]['firstName']
    lname = top_aban_init.iloc[i]['lastName']
    company = top_aban_init.iloc[i]['holdingCompanyName']
    aban_init = top_aban_init.iloc[i]['Abandoned Initiatives']
    print(f'{fname} {lname} - {company} - {aban_init}')
print(" ")
print('Initiative Exploration – Time Exploring Initiative Outputs: ')
print('---------------------------------')
print("Time Explored 0-5: " + str(init_expl5))
print("Time Explored 6-10: " + str(init_expl10))
print("Time Explored 11-15: " + str(init_expl15))
print("Time Explored 16-20: " + str(init_expl20))
print("Time Explored 21-30: " + str(init_expl30))
print("Time Explored 31-40: " + str(init_expl40))
print("Time Explored 41-50: " + str(init_expl50))
print("Time Explored 51-60: " + str(init_expl60))
print("Time Explored 61+:  " + str(init_expl61_plus))

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
print('Initiative Downloads')
print('---------------------------------')
print('Comp - Demo: ' + str(initdwn['Clicks for Measure: Initiative: Audience Insights: Composition - Demographics: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Audience Insights: Composition - Demographics: Download CSV'] > 0].shape[0]))
print('Comp - Interests: ' + str(initdwn['Clicks for Measure: Initiative: Audience Insights: Composition - Interests: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Audience Insights: Composition - Interests: Download CSV'] > 0].shape[0]))
print('Comp - Linear Consumption: ' + str(initdwn['Clicks for Measure: Initiative: Audience Insights: Composition - Linear Consumption: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Audience Insights: Composition - Linear Consumption: Download CSV'] > 0].shape[0]))
print('Delivery Breakdown - Table: ' + str(initdwn['Clicks for Measure: Initiative: Delivery: Cross-Screen - Delivery Breakdown: Table: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Delivery: Cross-Screen - Delivery Breakdown: Table: Download CSV'] > 0].shape[0]))
print('Digital: Delivery Breakdown: ' + str(initdwn['Clicks for Measure: Initiative: Delivery: Digital - Delivery Breakdown: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Delivery: Digital - Delivery Breakdown: Download CSV'] > 0].shape[0]))
print('Digital - Frequency Distribution: ' + str(initdwn['Clicks for Measure: Initiative: Delivery: Digital - Frequency Distribution: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Delivery: Digital - Frequency Distribution: Download CSV'] > 0].shape[0]))  
print('Linear: Delivery Breakdown: ' + str(initdwn['Clicks for Measure: Initiative: Delivery: Linear - Delivery Breakdown: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Delivery: Linear - Delivery Breakdown: Download CSV'] > 0].shape[0]))
print('Linear: Freq Distribution: ' + str(initdwn['Clicks for Measure: Initiative: Delivery: Linear - Frequency Distribution: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Delivery: Linear - Frequency Distribution: Download CSV'] > 0].shape[0]))
print('Attribution Discovery: ' + str(initdwn['Clicks for Measure: Initiative: Performance: Conversion - Attribution Discovery | CSV Download'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Performance: Conversion - Attribution Discovery | CSV Download'] > 0].shape[0]))
print('Perf Breakdown: Table: ' + str(initdwn['Clicks for Measure: Initiative: Performance: Detail - Performance Breakdown: Table: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Performance: Detail - Performance Breakdown: Table: Download CSV'] > 0].shape[0]))
print('Freq: Freq Distribution: ' + str(initdwn['Clicks for Measure: Initiative: Performance: Frequency - Frequency Distribution: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Performance: Frequency - Frequency Distribution: Download CSV'] > 0].shape[0]))
print('Digital Incremental Reach: ' + str(initdwn['Clicks for Measure: Initiative: Performance: Overlap - Digital Incremental Reach: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Performance: Overlap - Digital Incremental Reach: Download CSV'] > 0].shape[0]))
print('Network Duplication: ' + str(initdwn['Clicks for Measure: Initiative: Performance: Overlap - Network Duplication: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Performance: Overlap - Network Duplication: Download CSV'] > 0].shape[0]))
print('Platform Duplication: ' + str(initdwn['Clicks for Measure: Initiative: Performance: Overlap - Platform Duplication: Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiative: Performance: Overlap - Platform Duplication: Download CSV'] > 0].shape[0]))
print('Optimal Freq to Conversions: ' + str(initdwn['Clicks for Measure: Initiatives - Overview - Optimal Frequency to Conversions | Download CSV'].sum()) + ' - Users: '+ str(initdwn[initdwn['Clicks for Measure: Initiatives - Overview - Optimal Frequency to Conversions | Download CSV'] > 0].shape[0]))
print(' ')
print('MEASURE POWER USERS')
print('---------------------------------')
for i in range(init_launch5):
    fname = init_launch_power.iloc[i]['firstName']
    lname = init_launch_power.iloc[i]['lastName']
    company = init_launch_power.iloc[i]['holdingCompanyName']
    init_created = init_launch_power.iloc[i]['Clicks for Measure: Initiatives  - Create Initiative']
    init_launched = init_launch_power.iloc[i]['Clicks for Measure: Initiative: Setup - Launch Initiative']
    init_opened = init_launch_power.iloc[i]['Clicks for Measure: Initiatives - Initiative | Open']
    time_spent = init_launch_power.iloc[i]['Time On Page (minutes) for Measure: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {init_created} - Launched: {init_launched} - Opened: {init_opened} - {hours} hours {minutes} minutes')
## Currently allows for duplicates, can be made more efficient
for i in range(init_open10):
    fname = init_open_power.iloc[i]['firstName']
    lname = init_open_power.iloc[i]['lastName']
    company = init_open_power.iloc[i]['holdingCompanyName']
    init_created = init_open_power.iloc[i]['Clicks for Measure: Initiatives  - Create Initiative']
    init_launched = init_open_power.iloc[i]['Clicks for Measure: Initiative: Setup - Launch Initiative']
    init_opened = init_open_power.iloc[i]['Clicks for Measure: Initiatives - Initiative | Open']
    time_spent = init_open_power.iloc[i]['Time On Page (minutes) for Measure: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {init_created} - Launched: {init_launched} - Opened: {init_opened} - {hours} hours {minutes} minutes')
print(" ")
print('PLAN APP USAGE')
print('---------------------------------')
print('Total Users in App: ' + str(plan['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(plan_actives.shape[0]))
print('Average Time on App: ' + str(round(plan['Time On Page (minutes) for Plan: BUCKET'].mean(), 2)))
print('Average ACTIVE Time on App: ' + str(round(plan_actives['Time On Page (minutes) for Plan: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Time on App: ' + str(round(plan_nonactives['Time On Page (minutes) for Plan: BUCKET'].mean(), 2)))
print('Average Days on App: ' + str(round(plan['Days Active for Plan: BUCKET'].mean(), 2)))
print('Average ACTIVE Days on App: ' + str(round(plan_actives['Days Active for Plan: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Days on App: ' + str(round(plan_nonactives['Days Active for Plan: BUCKET'].mean(), 2)))
print(" ")
print('Created Plans: ' + str(plan['Clicks for Plan - Create Plan'].sum()))
print('Run Plans: ' + str(plan['Clicks for Plan: New Plan - Run Plan'].sum()))
print('Explored Plans: ' + str(plan['Clicks for Plan: Plans - Plan | Open'].sum()))
print('Linear Buys: ' + str(plan['Clicks for Plan: Plan: Linear Buy - Run Linear Buy'].sum()))
print('Aggregate Buys: ' + str(plan['Clicks for Plan: New Aggregate Buy - Run Aggregate Buy'].sum()))
print('Abandoned Plans: ' + str((plan['Clicks for Plan - Create Plan'].sum() - plan['Clicks for Plan: New Plan - Run Plan'].sum())))
print(" ")
print('Plan Exploration – Time Exploring Plan Outputs: ')
print('---------------------------------')
print("Time Explored 0-5: " + str(plan_expl5))
print("Time Explored 6-10: " + str(plan_expl10))
print("Time Explored 11-15: " + str(plan_expl15))
print("Time Explored 16-20: " + str(plan_expl20))
print("Time Explored 21-30: " + str(plan_expl30))
print("Time Explored 31-40: " + str(plan_expl40))
print("Time Explored 41-50: " + str(plan_expl50))
print("Time Explored 51-60: " + str(plan_expl60))
print("Time Explored 61+:  " + str(plan_expl61_plus))
print(" ")
print('Plan Exploration – Average vs. Median Page Views')
print('---------------------------------')
print('USERS')
print('---------------------------------')
print('Summary: ' + str(planexp[planexp['Page Views for Plan: Plan: Audience Insights: Summary'] > 0].shape[0]))
print('Discovery: ' + str(planexp[planexp['Page Views for Plan: Plan: Audience Insights: Discovery'] > 0].shape[0]))
print('Linear: ' + str(planexp[planexp['Page Views for Plan: Plan: Audience Insights: Linear'] > 0].shape[0]))
print('Overview: ' + str(planexp[planexp['Page Views for Plan: Plan: Linear Buys'] > 0].shape[0]))
print(' ')
print('AVERAGES - Page Views')
print('---------------------------------')
print('Summary: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Audience Insights: Summary'] > 0, 'Page Views for Plan: Plan: Audience Insights: Summary'].mean(), 2)))
print('Discovery: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Audience Insights: Discovery'] > 0, 'Page Views for Plan: Plan: Audience Insights: Discovery'].mean(), 2)))
print('Linear: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Audience Insights: Linear'] > 0, 'Page Views for Plan: Plan: Audience Insights: Linear'].mean(), 2)))
print('Overview: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Linear Buys'] > 0, 'Page Views for Plan: Plan: Linear Buys'].mean(), 2)))
print(' ')
print('MEDIAN - Page Views')
print('---------------------------------')
print('Summary: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Audience Insights: Summary'] > 0, 'Page Views for Plan: Plan: Audience Insights: Summary'].median(), 2)))
print('Discovery: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Audience Insights: Discovery'] > 0, 'Page Views for Plan: Plan: Audience Insights: Discovery'].median(), 2)))
print('Linear: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Audience Insights: Linear'] > 0, 'Page Views for Plan: Plan: Audience Insights: Linear'].median(), 2)))
print('Overview: ' + str(round(planexp.loc[planexp['Page Views for Plan: Plan: Linear Buys'] > 0, 'Page Views for Plan: Plan: Linear Buys'].median(), 2)))
print(' ')
print('AVERAGES - Time On Page')
print('---------------------------------')
print('Summary: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Audience Insights: Summary'] > 0, 'Time On Page (minutes) for Plan: Plan: Audience Insights: Summary'].mean(), 2)))
print('Discovery: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Audience Insights: Discovery'] > 0, 'Time On Page (minutes) for Plan: Plan: Audience Insights: Discovery'].mean(), 2)))
print('Linear: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Audience Insights: Linear'] > 0, 'Time On Page (minutes) for Plan: Plan: Audience Insights: Linear'].mean(), 2)))
print('Overview: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Linear Buys'] > 0, 'Time On Page (minutes) for Plan: Plan: Linear Buys'].mean(), 2)))
print(' ')
print('MEDIAN - Time On Page')
print('---------------------------------')
print('Summary: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Audience Insights: Summary'] > 0, 'Time On Page (minutes) for Plan: Plan: Audience Insights: Summary'].median(), 2)))
print('Discovery: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Audience Insights: Discovery'] > 0, 'Time On Page (minutes) for Plan: Plan: Audience Insights: Discovery'].median(), 2)))
print('Linear: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Audience Insights: Linear'] > 0, 'Time On Page (minutes) for Plan: Plan: Audience Insights: Linear'].median(), 2)))
print('Overview: ' + str(round(planexp.loc[planexp['Time On Page (minutes) for Plan: Plan: Linear Buys'] > 0, 'Time On Page (minutes) for Plan: Plan: Linear Buys'].median(), 2)))
print(' ')
print('PLAN POWER USERS')
print('---------------------------------')
for i in range(plan_run5):
    fname = plan_run_power.iloc[i]['firstName']
    lname = plan_run_power.iloc[i]['lastName']
    company = plan_run_power.iloc[i]['holdingCompanyName']
    plans_created = plan_run_power.iloc[i]['Clicks for Plan - Create Plan']
    plans_run = plan_run_power.iloc[i]['Clicks for Plan: New Plan - Run Plan']
    plans_opened = plan_run_power.iloc[i]['Clicks for Plan: Plans - Plan | Open']
    time_spent = plan_run_power.iloc[i]['Time On Page (minutes) for Plan: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {plans_created} - Launched: {plans_run} - Opened: {plans_opened} - {hours} hours {minutes} minutes')
## Currently allows for duplicates, can be made more efficient
for i in range(plan_open15):
    fname = plan_open_power.iloc[i]['firstName']
    lname = plan_open_power.iloc[i]['lastName']
    company = plan_open_power.iloc[i]['holdingCompanyName']
    plans_created = plan_open_power.iloc[i]['Clicks for Plan - Create Plan']
    plans_run = plan_open_power.iloc[i]['Clicks for Plan: New Plan - Run Plan']
    plans_opened = plan_open_power.iloc[i]['Clicks for Plan: Plans - Plan | Open']
    time_spent = plan_open_power.iloc[i]['Time On Page (minutes) for Plan: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {plans_created} - Launched: {plans_run} - Opened: {plans_opened} - {hours} hours {minutes} minutes')
    
print(" ")
print('BUY APP USAGE')
print('---------------------------------')
print('Total Users in App: ' + str(buy['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(buy_actives.shape[0]))
print('Average Time on App: ' + str(round(buy['Time On Page (minutes) for Buy: BUCKET'].mean(), 2)))
print('Average ACTIVE Time on App: ' + str(round(buy_actives['Time On Page (minutes) for Buy: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Time on App: ' + str(round(buy_nonactives['Time On Page (minutes) for Buy: BUCKET'].mean(), 2)))
print('Average Days on App: ' + str(round(buy['Days Active for Buy: BUCKET'].mean(), 2)))
print('Average ACTIVE Days on App: ' + str(round(buy_actives['Days Active for Buy: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Days on App: ' + str(round(buy_nonactives['Days Active for Buy: BUCKET'].mean(), 2)))
print(" ")
print('Created Plans: ' + str(buy['Clicks for Buy: Start Plan'].sum()))
print('Run Plans: ' + str(buy['Clicks for Buy: Plan Setup: Create Plan'].sum()))
print('Explored Plans: ' + str(buy['Clicks for Buy: Investment Plans - Plan | Open'].sum()))
print('Abandoned Plans: ' + str(buy['Clicks for Buy: Start Plan'].sum() - buy['Clicks for Buy: Plan Setup: Create Plan'].sum()))
print(" ")
print('BUY POWER USERS')
print('---------------------------------')
for i in range(buy_run5):
    fname = buy_run_power.iloc[i]['firstName']
    lname = buy_run_power.iloc[i]['lastName']
    company = buy_run_power.iloc[i]['holdingCompanyName']
    plans_created = buy_run_power.iloc[i]['Clicks for Buy: Start Plan']
    plans_run = buy_run_power.iloc[i]['Clicks for Buy: Plan Setup: Create Plan']
    plans_opened = buy_run_power.iloc[i]['Clicks for Buy: Investment Plans - Plan | Open']
    time_spent = buy_run_power.iloc[i]['Time On Page (minutes) for Buy: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {plans_created} - Launched: {plans_run} - Opened: {plans_opened} - {hours} hours {minutes} minutes')
##Currently allows for duplicates, can be made more efficient
for i in range(buy_open10):
    fname = buy_open_power.iloc[i]['firstName']
    lname = buy_open_power.iloc[i]['lastName']
    company = buy_open_power.iloc[i]['holdingCompanyName']
    plans_created = buy_open_power.iloc[i]['Clicks for Buy: Start Plan']
    plans_run = buy_open_power.iloc[i]['Clicks for Buy: Plan Setup: Create Plan']
    plans_opened = buy_open_power.iloc[i]['Clicks for Buy: Investment Plans - Plan | Open']
    time_spent = buy_open_power.iloc[i]['Time On Page (minutes) for Buy: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {plans_created} - Launched: {plans_run} - Opened: {plans_opened} - {hours} hours {minutes} minutes')
print(" ")
print('AUDIENCE APP USAGE')
print('---------------------------------')
print('Total Users in App: ' + str(audiences['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(audiences_actives.shape[0]))
print('Average Time on App: ' + str(round(audiences['Time On Page (minutes) for Audiences: BUCKET'].mean(), 2)))
print('Average ACTIVE Time on App: ' + str(round(audiences_actives['Time On Page (minutes) for Audiences: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Time on App: ' + str(round(audiences_nonactives['Time On Page (minutes) for Audiences: BUCKET'].mean(), 2)))
print('Average Days on App: ' + str(round(audiences['Days Active for Audiences: BUCKET'].mean(), 2)))
print('Average ACTIVE Days on App: ' + str(round(audiences_actives['Days Active for Audiences: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Days on App: ' + str(round(audiences_nonactives['Days Active for Audiences: BUCKET'].mean(), 2)))
print(" ")
print('Created Audiences: ' + str(audiences['Clicks for Audiences: Audiences - Create Audience'].sum()))
print('Saved Audiences: ' + str(audiences['Clicks for Audiences: New Audience - Create Audience'].sum()))
print('Explored Audiences: ' + str(audiences['Clicks for Audiences: Audiences - Audience | Open'].sum()))
print('TV Viewership Segments: ' + str(audiences['Clicks for Audiences: TV Viewership Segments - Create Segment'].sum()))
print('Abandoned Audiences: ' + str(audiences['Clicks for Audiences: Audiences - Create Audience'].sum() - audiences['Clicks for Audiences: New Audience - Create Audience'].sum()))
print('TV Viewership Started: ' + str(data['Clicks for Audiences: TV Viewership Segments - Create Segment'].sum()))
print('TV Viewership Created: ' + str(data['Clicks for Audiences: New TV Segment - Create Segment'].sum()))
print(" ")
print('AUDIENCE POWER USERS')
print('---------------------------------')
for i in range(audience_run5):
    fname = audience_run_power.iloc[i]['firstName']
    lname = audience_run_power.iloc[i]['lastName']
    company = audience_run_power.iloc[i]['holdingCompanyName']
    audience_created = audience_run_power.iloc[i]['Clicks for Audiences: Audiences - Create Audience']
    audience_run = audience_run_power.iloc[i]['Clicks for Audiences: New Audience - Create Audience']
    audience_opened = audience_run_power.iloc[i]['Clicks for Audiences: Audiences - Audience | Open']
    tvseg_start = audience_run_power.iloc[i]['Clicks for Audiences: TV Viewership Segments - Create Segment']
    tvseg_create = audience_run_power.iloc[i]['Clicks for Audiences: New TV Segment - Create Segment']
    time_spent = audience_run_power.iloc[i]['Time On Page (minutes) for Audiences: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {audience_created} - Launched: {audience_run} - Opened: {audience_opened} - TV Seg Started: {tvseg_start} - TV Seg Created: {tvseg_create} - {hours} hours {minutes} minutes')
##Currently allows for duplicates, can be made more efficient
for i in range(audience_open10):
    fname = audience_open_power.iloc[i]['firstName']
    lname = audience_open_power.iloc[i]['lastName']
    company = audience_open_power.iloc[i]['holdingCompanyName']
    audience_created = audience_open_power.iloc[i]['Clicks for Audiences: Audiences - Create Audience']
    audience_run = audience_open_power.iloc[i]['Clicks for Audiences: New Audience - Create Audience']
    audience_opened = audience_open_power.iloc[i]['Clicks for Audiences: Audiences - Audience | Open']
    tvseg_start = audience_open_power.iloc[i]['Clicks for Audiences: TV Viewership Segments - Create Segment']
    tvseg_create = audience_open_power.iloc[i]['Clicks for Audiences: New TV Segment - Create Segment']
    time_spent = audience_open_power.iloc[i]['Time On Page (minutes) for Audiences: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - Created: {audience_created} - Launched: {audience_run} - Opened: {audience_opened} - TV Seg Started: {tvseg_start} - TV Seg Created: {tvseg_create} - {hours} hours {minutes} minutes')
print(" ")
print('ALLOCATE APP USAGE')
print('---------------------------------')
print('Total Users in App: ' + str(allocate['Visitor ID'].shape[0]))
print('Total Active Users: ' + str(allocate_actives.shape[0]))
print('Average Time on App: ' + str(round(allocate['Time On Page (minutes) for Allocate: BUCKET'].mean(), 2)))
print('Average ACTIVE Time on App: ' + str(round(allocate_actives['Time On Page (minutes) for Allocate: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Time on App: ' + str(round(allocate_nonactives['Time On Page (minutes) for Allocate: BUCKET'].mean(), 2)))
print('Average Days on App: ' + str(round(allocate['Days Active for Allocate: BUCKET'].mean(), 2)))
print('Average ACTIVE Days on App: ' + str(round(allocate_actives['Days Active for Allocate: BUCKET'].mean(), 2)))
print('Average NON-ACTIVE Days on App: ' + str(round(allocate_nonactives['Days Active for Allocate: BUCKET'].mean(), 2)))
print(" ")
print('Run Allocations: ' + str(allocate['Clicks for Allocate: New Allocation - Run Allocation'].sum()))
print('Submitted Allocations: ' + str(allocate['Clicks for Allocate: Allocation - Submit to Mediaocean'].sum()))
print('Explored Allocations: ' + str(allocate['Clicks for Allocate: Allocations - Allocation | Open'].sum()))
print(" ")
print('TABLEAU')
print('---------------------------------')
print('Total Tableau Users: ' + str(tab_externals['username'].nunique()))
print('Total Tableau ACTIVES: ' + str(distinct_tabdates[distinct_tabdates['Number of Days Active'] >= 3].shape[0]))
print('Avg. Days in Tableau: ' + str(round(distinct_tabdates['Number of Days Active'].mean(), 2)))
print('Reports Accessed: ' + str(tab_externals.shape[0]))
print('Users in Tableau and The Platform: ' + str(tabxplat.shape[0]))
print('Users just in The Platform: ' + str(data.shape[0] - tabxplat.shape[0]))
print('Users just in Tableau: ' + str(distinct_tabusers - tabxplat.shape[0]))
print(" ")
print('CARD')
print('---------------------------------')
print('CARD Reports Accessed by HoldCo: ')
print(card_hc)
print(" ")
print('CARD Lite Reports Accessed by HoldCo:')
print(card_litehc)
print(" ")
print('CARD Users: ' + str(card['username'].nunique()))
print('CARD Active Users: ' + str(distinct_carddates[distinct_carddates['Number of Days Active'] >= 3].shape[0]))
print('Avg. Days in Tableau: ' + str(round(distinct_carddates['Number of Days Active'].mean(), 2)))
print('Reports Accessed: ' + str(card.shape[0]))
print('Holding Companies by Report Section: ')
print(card_byapp)
print(" ")
print('CARD Lite')
print('---------------------------------')
print('CARD Lite Users: ' + str(card_lite['username'].nunique()))
print('CARD Lite Active Users: ' + str(distinct_cardlitedates[distinct_cardlitedates['Number of Days Active'] >= 3].shape[0]))
print('Avg. Days in Tableau: ' + str(round(distinct_cardlitedates['Number of Days Active'].mean(), 2)))
print('Reports Accessed: ' + str(card_lite.shape[0]))
print('Holding Companies by Report Section: ')
print(cardlite_byapp)
print(" ")
print('Elsy Usage')
print('---------------------------------')
print('Total Users: ' + str(elsydata['Visitor ID'].nunique()))
print('Active Users: ' + str(elsydata[elsydata['Days Active'] >= 3].shape[0]))
print('Average Time on Elsy: ' + str(round(elsydata['Time on Site (minutes)'].mean(), 2)))
print('Average ACTIVE Time on Platform: ' + str(round(elsy_actives['Time on Site (minutes)'].mean(), 2)))
print('Average NON-ACTIVE Time on Platform: ' + str(round(elsy_nonactives['Time on Site (minutes)'].mean(), 2)))
print('Average Days on Elsy: ' + str(round(elsydata['Days Active'].mean(), 2)))
print('Average ACTIVE Days on Platform: ' + str(round(elsy_actives['Days Active'].mean(), 2)))
print('Average NON-ACTIVE Days on Platform: ' + str(round(elsy_nonactives['Days Active'].mean(), 2)))
print(" ")
print('Top Users By Time: ')
print(" ")
for i in range(8):
    fname = topelsytime.iloc[i]['firstName']
    lname = topelsytime.iloc[i]['lastName']
    company = topelsytime.iloc[i]['holdingCompanyName']
    time_spent = topelsytime.iloc[i]['Time on Site (minutes)']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - {hours} hours {minutes} minutes')
print(" ")
print('Top Users By Day: ')
print(" ")
for i in range(8):
    fname = topelsyday.iloc[i]['firstName']
    lname = topelsyday.iloc[i]['lastName']
    company = topelsyday.iloc[i]['holdingCompanyName']
    days = topelsyday.iloc[i]['Days Active']
    print(f'{fname} {lname} - {company} - {days} days')
print(" ")
print('Plan Overview Report: ')
print(" ")
print('USERS: ' + str(elsyrep[elsyrep['Time On Page (minutes) for Plan Overview Report: BUCKET'] > 0].shape[0]))
print('Average Time: ' + str(round(elsyrep.loc[elsyrep['Time On Page (minutes) for Plan Overview Report: BUCKET'] > 0, 'Time On Page (minutes) for Plan Overview Report: BUCKET'].mean(), 2)))
print('Average Views: ' + str(round(elsyrep.loc[elsyrep['Page Views for Plan Overview Report: BUCKET'] > 0, 'Page Views for Plan Overview Report: BUCKET'].mean(), 2)))
print('Top Users: ')
print(" ")
for i in range(8):
    fname = topelsy_po_time.iloc[i]['firstName']
    lname = topelsy_po_time.iloc[i]['lastName']
    company = topelsy_po_time.iloc[i]['holdingCompanyName']
    time_spent = topelsy_po_time.iloc[i]['Time On Page (minutes) for Plan Overview Report: BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - {hours} hours {minutes} minutes')  
print(" ")
print('Plan Comparison Report: ')
print(" ")
print('USERS: ' + str(elsyrep[elsyrep['Time On Page (minutes) for Elsy: Plan Comparison Report - BUCKET'] > 0].shape[0]))
print('Average Time: ' + str(round(elsyrep.loc[elsyrep['Time On Page (minutes) for Elsy: Plan Comparison Report - BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Plan Comparison Report - BUCKET'].mean(), 2)))
print('Average Views: ' + str(round(elsyrep.loc[elsyrep['Page Views for Elsy: Plan Comparison Report - BUCKET'] > 0, 'Page Views for Elsy: Plan Comparison Report - BUCKET'].mean(), 2)))
print('Top Users: ')
print(" ")
for i in range(8):
    fname = topelsy_pc_time.iloc[i]['firstName']
    lname = topelsy_pc_time.iloc[i]['lastName']
    company = topelsy_pc_time.iloc[i]['holdingCompanyName']
    time_spent = topelsy_pc_time.iloc[i]['Time On Page (minutes) for Elsy: Plan Comparison Report - BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - {hours} hours {minutes} minutes')
print(" ")
print('Campaign Performance Report: ')
print(" ")
print('USERS: ' + str(elsyrep[elsyrep['Time On Page (minutes) for Elsy: Campaign Performance Report - BUCKET'] > 0].shape[0]))
print('Average Time: ' + str(round(elsyrep.loc[elsyrep['Time On Page (minutes) for Elsy: Campaign Performance Report - BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Campaign Performance Report - BUCKET'].mean(), 2)))
print('Average Views: ' + str(round(elsyrep.loc[elsyrep['Page Views for Elsy: Campaign Performance Report - BUCKET'] > 0, 'Page Views for Elsy: Campaign Performance Report - BUCKET'].mean(), 2)))
print('Top Users: ')
print(" ")
for i in range(8):
    fname = topelsy_cp_time.iloc[i]['firstName']
    lname = topelsy_cp_time.iloc[i]['lastName']
    company = topelsy_cp_time.iloc[i]['holdingCompanyName']
    time_spent = topelsy_cp_time.iloc[i]['Time On Page (minutes) for Elsy: Campaign Performance Report - BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - {hours} hours {minutes} minutes')
print(" ")
print('Campaign Monitoring Report: ')
print(" ")
print('USERS: ' + str(elsyrep[elsyrep['Time On Page (minutes) for Elsy: Campaign Monitoring Report - BUCKET'] > 0].shape[0]))
print('Average Time: ' + str(round(elsyrep.loc[elsyrep['Time On Page (minutes) for Elsy: Campaign Monitoring Report - BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Campaign Monitoring Report - BUCKET'].mean(), 2)))
print('Average Views: ' + str(round(elsyrep.loc[elsyrep['Page Views for Elsy: Campaign Monitoring Report - BUCKET'] > 0, 'Page Views for Elsy: Campaign Monitoring Report - BUCKET'].mean(), 2)))
print('Top Users: ')
print(" ")
for i in range(8):
    fname = topelsy_cm_time.iloc[i]['firstName']
    lname = topelsy_cm_time.iloc[i]['lastName']
    company = topelsy_cm_time.iloc[i]['holdingCompanyName']
    time_spent = topelsy_cm_time.iloc[i]['Time On Page (minutes) for Elsy: Campaign Monitoring Report - BUCKET']
    hours, minutes = divmod(time_spent, 60)
    print(f'{fname} {lname} - {company} - {hours} hours {minutes} minutes')
print(' ')
print('Elsy Pages')
print('---------------------------------')
print('USERS')
print('---------------------------------')
print('Home Screen: ' + str(elsydata[elsydata['Page Views for Elsy: Home'] > 0].shape[0]))
print('Instance Overview: ' + str(elsydata[elsydata['Page Views for Elsy: Instance: Overview'] > 0].shape[0]))
print('Instance Product List: ' + str(elsydata[elsydata['Page Views for Elsy: Instance: Product List'] > 0].shape[0]))
print('Campaign List: ' + str(elsydata[elsydata['Page Views for Elsy: Campaign List: BUCKET'] > 0].shape[0]))
print('Reports: ' + str(elsydata[elsydata['Page Views for Elsy: Reports: BUCKET'] > 0].shape[0]))
print('Research Media Vehicles: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Media Vehicles: BUCKET'] > 0].shape[0]))
print('Research Audiences: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Audiences: BUCKET'] > 0].shape[0]))
print('Research Locations: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Locations: BUCKET'] > 0].shape[0]))
print('Research Inventory Sources: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Inventory Sources: BUCKET'] > 0].shape[0]))
print('Research Segments: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Segments: BUCKET'] > 0].shape[0]))
print('Research DMPSs: ' + str(elsydata[elsydata['Page Views for Elsy: Research: DMPs: BUCKET'] > 0].shape[0]))
print('Research Activation Platforms: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Activation Platforms: BUCKET'] > 0].shape[0]))
print('Research Activation Partners: ' + str(elsydata[elsydata['Page Views for Elsy: Research: Activation Partners: BUCKET'] > 0].shape[0]))
print('Research News & Notifications: ' + str(elsydata[elsydata['Page Views for Elsy: Research: News & Notifications'] > 0].shape[0]))
print('Datamart: ' + str(elsydata[elsydata['Page Views for Elsy: Datamart: BUCKET'] > 0].shape[0]))
print(' ')
print(' ')
print('AVERAGE ELSY PAGES')
print('---------------------------------')
print('Home Screen: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Home'] > 0, 'Page Views for Elsy: Home'].mean(), 2)))
print('Instance Overview: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Instance: Overview'] > 0, 'Page Views for Elsy: Instance: Overview'].mean(), 2)))
print('Instance Product List: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Instance: Product List'] > 0, 'Page Views for Elsy: Instance: Product List'].mean(), 2)))
print('Campaign List: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Campaign List: BUCKET'] > 0, 'Page Views for Elsy: Campaign List: BUCKET'].mean(), 2)))
print('Reports: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Reports: BUCKET'] > 0, 'Page Views for Elsy: Reports: BUCKET'].mean(), 2)))
print('Research Media Vehicles: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Media Vehicles: BUCKET'] > 0, 'Page Views for Elsy: Research: Media Vehicles: BUCKET'].mean(), 2)))
print('Research Audiences: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Audiences: BUCKET'] > 0, 'Page Views for Elsy: Research: Audiences: BUCKET'].mean(), 2)))
print('Research Locations: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Locations: BUCKET'] > 0, 'Page Views for Elsy: Research: Locations: BUCKET'].mean(), 2)))
print('Research Inventory Sources: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Inventory Sources: BUCKET'] > 0, 'Page Views for Elsy: Research: Inventory Sources: BUCKET'].mean(), 2)))
print('Research Segments: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Segments: BUCKET'] > 0, 'Page Views for Elsy: Research: Segments: BUCKET'].mean(), 2)))
print('Research DMPSs: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: DMPs: BUCKET'] > 0, 'Page Views for Elsy: Research: DMPs: BUCKET'].mean(), 2)))
print('Research Activation Platforms: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Activation Platforms: BUCKET'] > 0, 'Page Views for Elsy: Research: Activation Platforms: BUCKET'].mean(), 2)))
print('Research Activation Partners: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Activation Partners: BUCKET'] > 0, 'Page Views for Elsy: Research: Activation Partners: BUCKET'].mean(), 2)))
print('Research News & Notifications: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: News & Notifications'] > 0, 'Page Views for Elsy: Research: News & Notifications'].mean(), 2)))
print('Datamart: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Datamart: BUCKET'] > 0, 'Page Views for Elsy: Datamart: BUCKET'].mean(), 2)))
print(' ')
print('MEDIAN ELSY PAGES')
print('---------------------------------')
print('Home Screen: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Home'] > 0, 'Page Views for Elsy: Home'].median(), 2)))
print('Instance Overview: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Instance: Overview'] > 0, 'Page Views for Elsy: Instance: Overview'].median(), 2)))
print('Instance Product List: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Instance: Product List'] > 0, 'Page Views for Elsy: Instance: Product List'].median(), 2)))
print('Campaign List: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Campaign List: BUCKET'] > 0, 'Page Views for Elsy: Campaign List: BUCKET'].median(), 2)))
print('Reports: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Reports: BUCKET'] > 0, 'Page Views for Elsy: Reports: BUCKET'].median(), 2)))
print('Research Media Vehicles: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Media Vehicles: BUCKET'] > 0, 'Page Views for Elsy: Research: Media Vehicles: BUCKET'].median(), 2)))
print('Research Audiences: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Audiences: BUCKET'] > 0, 'Page Views for Elsy: Research: Audiences: BUCKET'].median(), 2)))
print('Research Locations: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Locations: BUCKET'] > 0, 'Page Views for Elsy: Research: Locations: BUCKET'].median(), 2)))
print('Research Inventory Sources: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Inventory Sources: BUCKET'] > 0, 'Page Views for Elsy: Research: Inventory Sources: BUCKET'].median(), 2)))
print('Research Segments: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Segments: BUCKET'] > 0, 'Page Views for Elsy: Research: Segments: BUCKET'].median(), 2)))
print('Research DMPSs: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: DMPs: BUCKET'] > 0, 'Page Views for Elsy: Research: DMPs: BUCKET'].median(), 2)))
print('Research Activation Platforms: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Activation Platforms: BUCKET'] > 0, 'Page Views for Elsy: Research: Activation Platforms: BUCKET'].median(), 2)))
print('Research Activation Partners: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: Activation Partners: BUCKET'] > 0, 'Page Views for Elsy: Research: Activation Partners: BUCKET'].median(), 2)))
print('Research News & Notifications: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Research: News & Notifications'] > 0, 'Page Views for Elsy: Research: News & Notifications'].median(), 2)))
print('Datamart: ' + str(round(elsydata.loc[elsydata['Page Views for Elsy: Datamart: BUCKET'] > 0, 'Page Views for Elsy: Datamart: BUCKET'].median(), 2)))
print(' ')
print('AVERAGE ELSY TIME')
print('---------------------------------')
print('Home Screen: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Home'] > 0, 'Time On Page (minutes) for Elsy: Home'].mean(), 2)))
print('Instance Overview: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Instance: Overview'] > 0, 'Time On Page (minutes) for Elsy: Instance: Overview'].mean(), 2)))
print('Instance Product List: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Instance: Product List'] > 0, 'Time On Page (minutes) for Elsy: Instance: Product List'].mean(), 2)))
print('Campaign List: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Campaign List: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Campaign List: BUCKET'].mean(), 2)))
print('Reports: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Reports: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Reports: BUCKET'].mean(), 2)))
print('Research Media Vehicles: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Media Vehicles: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Media Vehicles: BUCKET'].mean(), 2)))
print('Research Audiences: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Audiences: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Audiences: BUCKET'].mean(), 2)))
print('Research Locations: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Locations: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Locations: BUCKET'].mean(), 2)))
print('Research Inventory Sources: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Inventory Sources: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Inventory Sources: BUCKET'].mean(), 2)))
print('Research Segments: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Segments: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Segments: BUCKET'].mean(), 2)))
print('Research DMPSs: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: DMPs: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: DMPs: BUCKET'].mean(), 2)))
print('Research Activation Platforms: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Activation Platforms: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Activation Platforms: BUCKET'].mean(), 2)))
print('Research Activation Partners: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Activation Partners: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Activation Partners: BUCKET'].mean(), 2)))
print('Research News & Notifications: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: News & Notifications'] > 0, 'Time On Page (minutes) for Elsy: Research: News & Notifications'].mean(), 2)))
print('Datamart: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Datamart: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Datamart: BUCKET'].mean(), 2)))
print(' ')
print('MEDIAN ELSY TIME')
print('---------------------------------')
print('Home Screen: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Home'] > 0, 'Time On Page (minutes) for Elsy: Home'].median(), 2)))
print('Instance Overview: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Instance: Overview'] > 0, 'Time On Page (minutes) for Elsy: Instance: Overview'].median(), 2)))
print('Instance Product List: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Instance: Product List'] > 0, 'Time On Page (minutes) for Elsy: Instance: Product List'].median(), 2)))
print('Campaign List: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Campaign List: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Campaign List: BUCKET'].median(), 2)))
print('Reports: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Reports: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Reports: BUCKET'].median(), 2)))
print('Research Media Vehicles: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Media Vehicles: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Media Vehicles: BUCKET'].median(), 2)))
print('Research Audiences: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Audiences: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Audiences: BUCKET'].median(), 2)))
print('Research Locations: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Locations: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Locations: BUCKET'].median(), 2)))
print('Research Inventory Sources: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Inventory Sources: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Inventory Sources: BUCKET'].median(), 2)))
print('Research Segments: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Segments: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Segments: BUCKET'].median(), 2)))
print('Research DMPSs: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: DMPs: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: DMPs: BUCKET'].median(), 2)))
print('Research Activation Platforms: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Activation Platforms: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Activation Platforms: BUCKET'].median(), 2)))
print('Research Activation Partners: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: Activation Partners: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Research: Activation Partners: BUCKET'].median(), 2)))
print('Research News & Notifications: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Research: News & Notifications'] > 0, 'Time On Page (minutes) for Elsy: Research: News & Notifications'].median(), 2)))
print('Datamart: ' + str(round(elsydata.loc[elsydata['Time On Page (minutes) for Elsy: Datamart: BUCKET'] > 0, 'Time On Page (minutes) for Elsy: Datamart: BUCKET'].median(), 2)))