import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

# df = pd.read_csv('data/2016 Stack Overflow Survey Responses.csv')
# print(df)
# pd.to_pickle(df, 'data/SOpickle')

df = pd.read_pickle('data/SOpickle')
# print(list(df))
country = np.array(df['country'].data)
soregion = np.array(df['so_region'].data)
age = np.array(df['age_midpoint'].data)
gender = np.array(df['gender'].data)
occupation = np.array(df['occupation'].data)
experience = np.array(df['experience_midpoint'].data)
salary = np.array(df['salary_midpoint'].data)
aliens = np.array(df['aliens'].data)
ability = np.array(df['programming_ability'].data)
status = np.array(df['employment_status'].data)
industry = np.array(df['industry'].data)
companysize = np.array(df['company_size_range'].data)
teamsize = np.array(df['team_size_range'].data)
women = np.array(df['women_on_team'].data)
remote = np.array(df['remote'].data)
jobsatisfaction = np.array(df['job_satisfaction'].data)
pet = np.array(df['dogs_vs_cats'].data)
education = np.array(df['education'].data)
star = np.array(df['star_wars_vs_star_trek'].data)
atech = np.array(df['agree_tech'].data)
anotice = np.array(df['agree_notice'].data)
aproblem = np.array(df['agree_problemsolving'].data)
adiversity = np.array(df['agree_diversity'].data)
aadblocker = np.array(df['agree_adblocker'].data)
aalcohol = np.array(df['agree_alcohol'].data)
aboss = np.array(df['agree_loveboss'].data)
anight = np.array(df['agree_nightcode'].data)
alegacy = np.array(df['agree_legacy'].data)
amars = np.array(df['agree_mars'].data)
ivariety = np.array(df['important_variety'].data)
icontrol = np.array(df['important_control'].data)
isameend = np.array(df['important_sameend'].data)
inewtech = np.array(df['important_newtech'].data)
ibuildnew = np.array(df['important_buildnew'].data)
ibuildexisting = np.array(df['important_buildexisting'].data)
ipromotion = np.array(df['important_promotion'].data)
imission = np.array(df['important_companymission'].data)
iwfh = np.array(df['important_wfh'].data)
ioffice = np.array(df['important_ownoffice'].data)
challenges = np.array(df['developer_challenges'].data)
whystack = np.array(df['why_stack_overflow'].data)
interview = np.array(df['how_to_improve_interview_process'].data)
jobsearch = np.array(df['job_search_annoyance'].data)
newjob = np.array(df['open_to_new_job'].data)
jobvalue = np.array(df['new_job_value'].data)

def agreevalue(x):
    if x == 'Disagree completely':
        x = random.randint(0, 3) / 100
    elif x == 'Disagree somewhat':
        x = random.randint(24, 27) / 100
    elif x == 'Neutral':
        x = random.randint(49, 52) / 100
    elif x == 'Agree somewhat':
        x = random.randint(69, 72) / 100
    elif x == 'Agree completely':
        x = random.randint(97, 100) / 100
    # else:
    #     x == 0.5
    return x


def agree():
    choices = ['Disagree completely', 'Disagree somewhat', 'Neutral', 'Agree somewhat', 'Agree completely']
    indx = 0
    idxlist = []
    for i in range(len(atech)):
        # , anotice, aproblem, adiversity, aadblocker, aalcohol, aboss, anight, alegacy, amars):
        if type(atech[i]) is str and type(anotice[i]) is str and type(aproblem[i]) is str and \
                type(adiversity[i]) is str and type(aadblocker[i]) is str and type (aalcohol[i]) is str and \
                type(aboss[i]) is str and type(anight[i]) is str and type(alegacy[i]) is str and type(amars[i]) is str:
           # and type(p) is str and type(ad) is str and type(ab) is str and type(al) and \
           #              type(b) is str and type(ni) is str and type(l) is str and type(m) is str:
            idxlist.append(indx)
            # indx += 1
            atech[i] = agreevalue(atech[i])
            anotice[i] = agreevalue(anotice[i])
            aproblem[i] = agreevalue(aproblem[i])
            adiversity[i] = agreevalue(adiversity[i])
            aadblocker[i] = agreevalue(aadblocker[i])
            aalcohol[i] = agreevalue(aalcohol[i])
            aboss[i] = agreevalue(aboss[i])
            anight[i] = agreevalue(anight[i])
            alegacy[i] = agreevalue(alegacy[i])
            amars[i] = agreevalue(amars[i])
        indx += 1

    regionset = set(soregion)
    regionset = sorted([x for x in regionset if x == x])
    # regionset = ['Africa', 'Antarctica', 'Caribbean', 'Central America', 'Central Asia', 'East Asia',
    #  'Eastern Europe', 'Middle East', 'North America', 'Oceania', 'South America', 'South Asia',
    #  'Southeast Asia', 'Western Europe']

    for i in idxlist:
        if soregion[i] == regionset[8]:
        # for i in range(100):
            plt.plot([0, 1], [atech[i], anotice[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([1, 2], [anotice[i], aproblem[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([2, 3], [aproblem[i], adiversity[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([3, 4], [adiversity[i], aadblocker[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([4, 5], [aadblocker[i], aalcohol[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([5, 6], [aalcohol[i], aboss[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([6, 7], [aboss[i], anight[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([7, 8], [anight[i], alegacy[i]], color='g', lw=.3)
        # for i in range(100):
            plt.plot([8, 9], [alegacy[i], amars[i]], color='g', lw=.3)
    plt.text(-1, 0.05, s='Disagree C', va='top', ha='center')
    plt.text(-1, 0.27, s='Disagree S', va='top', ha='center')
    plt.text(-1, 0.52, s='N', va='top', ha='center')
    plt.text(-1, 0.73, s='Agree S', va='top', ha='center')
    plt.text(-1, 1, s='Aagree C', va='top', ha='center')
    plt.text(0, 0, s='tech', va='top', ha='center')
    plt.text(1, 0, s='notice', va='top', ha='center')
    plt.text(2, 0, s='problem', va='top', ha='center')
    plt.text(3, 0, s='diversity', va='top', ha='center')
    plt.text(4, 0, s='adblocker', va='top', ha='center')
    plt.text(5, 0, s='alcohol', va='top', ha='center')
    plt.text(6, 0, s='boss', va='top', ha='center')
    plt.text(7, 0, s='night', va='top', ha='center')
    plt.text(8, 0, s='legacy', va='top', ha='center')
    plt.text(9, 0, s='mars', va='top', ha='center')

    ax = plt.gca()
    ax.axis('off')

    plt.show()


def main():
    agree()
    # regionset = set(soregion)
    # regionset = sorted([x for x in regionset if x == x])
    # print(regionset)



if __name__ == '__main__':
    main()

