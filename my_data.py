# # create dictionary to hold dates and hours coded
dict_2020 = {'Sept_November':196,
'11/24/20':1,
'11/25/20': 3,
'11/26/20':.5,
'11/27/20':.25,
'11/28/20':.5, 
'11/29/20':2.5,
'11/30/20': .5,
'12/1/20':1,
'12/2/20':2.5,
'12/3/20':1,
'12/4/20':2.5,
'12/5/20':.75, 
'12/6/20':.25,
'12/8/20':.5,
'12/12/20':3.5,
'12/13/20': .1,
'12/17/20':1,
'12/18/2020':3,
'12/19/2020': 2.5, 
'12/20/2020': .25, 
'12/21/2020': 1.75,
'12/22/2020': 1.25, 
'12/25/2020': .5, 
'12/26/2020': 2, 
'12/27/2020': 2.25, 
'12/28/2020': .75, 
'12/29/2020':2.5,
'12/30/2020':3,
'12/31/2020':2, 
'01/01/2021':1, 
'01/02/2021':2, 
'01/03/2021': 1.75, 
'01/04/2021':1.75, 
'01/05/2020':1, 
'01/09/2020':2,
'01/10/2020':.5, 
'01/11/2020':.5, 
'01/12/2020':.75,
'01/13/2020':.20,
'01/14/2020':.1,
'01/15/2020':.1, 
'01/16/2020':1.25,
'01/19/2020':.1,
'01/22/2021':1,
'01/23/2021':.25,
'01/24/2021':.25,
'01/25/2021':.25,
'1/25/2021':.5,
'1/30/2021':.5,
'02/05/2021':2, 
'02/06/2021':1,
'02/07/2021':1.5,
'02/08/2021':1,
'02/09/2021':.25,
'02/09/2021':.5,
'02/13/2021':1, 
'02/14/2021': 1.75, 
'02/15/2021':1.25, 
'2/17/2021': .5,
'2/18/2021':.25, 
'2/20/2021':1, 
'2/23/2021':1,
'2/24/2021':.5, 
'2/25/2021':1.5, 
'2/26/2021':.5,
'2/28/2021':1.5,
'3/1/2021':1.5,
'3/2/2021':1.5, 
'3/3/2021':2.5, 
'3/4/2021':3,
'3/8/2021':2,
'3/9/2021':1, 
'3/11/2021':1 , 
'3/11/2021':2,
'3/12/2021':2, 
'3/13/2021':3,
'3/15/2021':3,
'3/19/2021':2, 
'3/20/2020':2.5,
'3/21/2020':2,
'3/27/2021':.4, 
'3/28/2021':.6,
'3/31/2021':.75, 
'4/2/2021':2, 
'4/5/2021':1, 
'4/6/2021':.5, 
'4/7/2021':.5, 
'4/10/2021':.5, 
'4/11/2021':1, 
'4/14/2021':1, 
'4/17/2021':.25, 
'4/18/2021':.75, 
'4/20/2021':1.75, 
'4/21/2021':3,
'4/24/2021': 1.5, 
'4/25/2021': 2, 
'4/27/2021':2.5, 
'4/28/2021':2, 
'4/29/2021':1.4, 
'4/30/2021':.5,
'5/02/2021': 1.5, 
'5/10/2021' : 3, 
'5/11/2021':4, 
'5/12/2021':5, 
'5/13/2021':1, 
'5/14/2021':5, 
'5/15/2021':2,
'5/16/2021': 1, 
'5/17/2021':1.5, 
'5/18/2021': 2, 
'5/19/2021':1.5, 
'5/20/2021':4, 
'5/22/2021':4,
'5/25/2021':3, 
'5/26/2021':2, 
'5/27/2021': 2, 
'5/28/2021':2, 
'5/29/2021': 2, 
'5/30/2021': 2,
'5/31/2021':1, 
'6/01/2021':1, 
'06/02/2021':3, 
'06/03/2021': 1.5, 
'06/04/2021':.75, 
'06/07/2021': 1.5, 
'06/08/2021':2.25,
'06/09/2021':.25, 
'06/10/2021': 1.75, 
'06/16/2021': 3.75, 
'06/17/2021': 1.25, 
'06/18/2021':4, 
'06/19/2021': 1, 
'06/20/2021':1,
'06/22/2021': .25, 
'06/23/2021':1, 
'06/24/2021':2, 
'06/25/2021':3, 
'06/26/2021': 2, 
'06/27/2021': 1, 
'07/06/2021': 2.5, 
'07/07/2021':4, 
'07/08/2021':4, 
'07/09/2021': 4, 
'07/17/2021':2, 
'07/18/2021':1, 
'07/19/2021':2, 
'07/20/2021':1.5,
'07/21/2021': .25, 
'07/22/2021':3, 
'07/23/2021':2.5, 
'07/26/2021':1, 
'7/27/2021': 1.25, 
'7/28/2021':1,
'07/29/2021': 2, 
'07/30/2021': 1, 
'08/01/2021':1.5, 
'08/03/2021': 1, 
'08/04/2021': .5, 
'08/05/2021': 3, 
'08/06/2021':2,
'08/11/2021': 1, 
'08/12/2021':0, 
'08/25/2021':2.5, 
'08/26/2021':4, 
'08/30/2021':3, 
'08/31/2021': 2,
'09/01/2021': .5, 
'09/03/2021': 1, 
'09/04/2021':1.5, 
'09/06/2021':1, 
'09/07/2021': 1, 
'09/02021':.5,
'09/10/2021': .45, 
'09/13/2021': 1.50, 
'09/14/2021': .5, 
'09/15/2021': .25, 
'09/20/2021': 1, '09/22/2021': 4, '09/27/2021':1.5,
'09/30/2021': 1, 
'09/30/2021': 1, 
'10/02/2021': 2, 
'10/3/2021':3.5, 
'10/4/2021': 1, 
'10/5/2021':1,
'10/07/2021':2, 
'10/08/2021':3, 
'10/09/2021': 2, 
'10/11/2021': 2.5, 
'10/13/2021': 1, 
'10/14/2021': 2, 
"10/15/2021": 2, 
"10/16/2021":1,
'10/17/2021': 1.45,
'10/18/2021':1




}


hours= dict_2020.values()
#print(hours)


# # make another variable..this seems to complicated!
total = sum(hours)
print(total)
#total hours for goal and next benchmark
goal = 3000
# variable for new benchmark
big_milestone = 500
# hours left until next benchmark
mini_milestone = 425

hours_until_mini_mile = mini_milestone - total

hours_untill_nb = big_milestone - total
#half way mark
half_way = 1500
# next small benchmark
mini_bench = 400

mini_mini = 470
# hours to mini bench
hours_untill = mini_mini - total

hours_mini_bench = mini_bench - total

progress = total / goal
print(progress)
# # # print total of values

print(f"Your goal is to code for {goal} hours. As of today You have coded for {format(total, '.2f')} hours!")

print(f"Right now you are {format(progress, '.2%')} of the way to your goal!")


print(f"You are just {format(hours_untill_nb, '.2f')} hours from your next benchmark")

#print(f"YOu are just {format(hours_until_mini_mile, '.2f')} from your next mini-milestone.")

#print(f"You are just {format(hours_mini_bench, '.2f')} hours until your next mini-bench mark")

print(f"You are just {format(hours_untill, '.2f')} hours from your next mini-mini-bench mark")





# doing = ['Covid 19 ML Predictions.','Ranked order for USTA',
# 'Building Dashboard with Seaborn for USTA','Time Log',
# "Why is LogisticRegression() not working?!"
# 'working on merges, manipulating dataframes..wouldnt this be easier in SQL?',
# 'building weather predictor', 'used glob to join multiple files..cool!',
# 'created dashboard for NTRP','Historical Minneapolis Weather',
# 'Experimental Poetics Project','Days Alive', 'life summary in code',
# 'functions measuring time alive','crazy dumb index thing problem, solved \
# by writing df to file and then loading back',
# 'building random sentencem generator from literary wprk',
# 'building rock-paper-scissors game', 'using query','plotting investments']

# #for i in doing:
#     #print(doing)



