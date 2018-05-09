import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib import colors as mcolors

import math

df = pd.read_csv('data/2016 Stack Overflow Survey Responses.csv')
# print(df)
pd.to_pickle(df, 'data/SOpickle')

df = pd.read_pickle('data/SOpickle')
# print(list(df))
country = np.array(df['country'].data)
soregion = np.array(df['so_region'].data)  #stack overflow region
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
remote = np.array(df['remote'].data) #how often do you work remotely
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
        x = random.randint(0, 10) / 1000
    elif x == 'Disagree somewhat':
        x = random.randint(240, 250) / 1000
    elif x == 'Neutral':
        x = random.randint(490, 500) / 1000
    elif x == 'Agree somewhat':
        x = random.randint(740, 750) / 1000
    elif x == 'Agree completely':
        x = random.randint(990, 1000) / 1000
    # else:
    #     x == 0.5
    return x

def importancevalue(x):
    if x == "I don't care about this":
        x = random.randint(0, 10) / 1000
    elif x == 'This is somewhat important':
        x = x = random.randint(490, 500) / 1000
    elif x == 'This is very important':
        x = x = random.randint(990, 1000) / 1000

    return x


def agree():
    # choices = ['Disagree completely', 'Disagree somewhat', 'Neutral', 'Agree somewhat', 'Agree completely']

    regionset = set(soregion)
    regionset = sorted([x for x in regionset if x == x])
    # regionset = ['Africa', 'Antarctica', 'Caribbean', 'Central America', 'Central Asia', 'East Asia',
    #  'Eastern Europe', 'Middle East', 'North America', 'Oceania', 'South America', 'South Asia',
    #  'Southeast Asia', 'Western Europe']

    avglist = []

    for region in regionset:
        indx = 0
        idxlist = []
        atechavg = 0
        anoticeavg = 0
        aproblemavg = 0
        adiversityavg = 0
        aadblockervg = 0
        aalcoholavg = 0
        abossavg = 0
        anightavg = 0
        alegacyavg = 0
        amarsvg = 0

        for i in range(len(atech)):
            if len(idxlist) < 100:
                if type(atech[i]) is str and type(anotice[i]) is str and type(aproblem[i]) is str and \
                        type(adiversity[i]) is str and type(aadblocker[i]) is str and type (aalcohol[i]) is str and \
                        type(aboss[i]) is str and type(anight[i]) is str and type(alegacy[i]) is str and type(amars[i]) is str:
                    idxlist.append(indx)
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

                    atechavg += atech[i]
                    anoticeavg += anotice[i]
                    aproblemavg += aproblem[i]
                    adiversityavg += adiversity[i]
                    aadblockervg += aadblocker[i]
                    aalcoholavg += aalcohol[i]
                    abossavg += aboss[i]
                    anightavg += anight[i]
                    alegacyavg += alegacy[i]
                    amarsvg += amars[i]

                indx += 1

        if len(idxlist) > 0:
            atechavg /= len(idxlist)
            anoticeavg /= len(idxlist)
            aproblemavg /= len(idxlist)
            adiversityavg /= len(idxlist)
            aadblockervg /= len(idxlist)
            aalcoholavg /= len(idxlist)
            abossavg /= len(idxlist)
            anightavg /= len(idxlist)
            alegacyavg /= len(idxlist)
            amarsvg /= len(idxlist)

            plt.rcParams["figure.figsize"] = [10.0, 8.0]

            for i in idxlist:
                plt.plot([0, 1], [atech[i], anotice[i]], color='c', lw=.3)
                plt.plot([1, 2], [anotice[i], aproblem[i]], color='c', lw=.3)
                plt.plot([2, 3], [aproblem[i], adiversity[i]], color='c', lw=.3)
                plt.plot([3, 4], [adiversity[i], aadblocker[i]], color='c', lw=.3)
                plt.plot([4, 5], [aadblocker[i], aalcohol[i]], color='c', lw=.3)
                plt.plot([5, 6], [aalcohol[i], aboss[i]], color='c', lw=.3)
                plt.plot([6, 7], [aboss[i], anight[i]], color='c', lw=.3)
                plt.plot([7, 8], [anight[i], alegacy[i]], color='c', lw=.3)
                plt.plot([8, 9], [alegacy[i], amars[i]], color='c', lw=.3)

            plt.plot([0, 1], [atechavg, anoticeavg], color='r', lw=2)
            plt.plot([1, 2], [anoticeavg, aproblemavg], color='r', lw=2)
            plt.plot([2, 3], [aproblemavg, adiversityavg], color='r', lw=2)
            plt.plot([3, 4], [adiversityavg, aadblockervg], color='r', lw=2)
            plt.plot([4, 5], [aadblockervg, aalcoholavg], color='r', lw=2)
            plt.plot([5, 6], [aalcoholavg, abossavg], color='r', lw=2)
            plt.plot([6, 7], [abossavg, anightavg], color='r', lw=2)
            plt.plot([7, 8], [anightavg, alegacyavg], color='r', lw=2)
            plt.plot([8, 9], [alegacyavg, amarsvg], color='r', lw=2)

            avglist.append([atechavg, anoticeavg, aproblemavg, adiversityavg, aadblockervg, aalcoholavg, abossavg,
                            anightavg, alegacyavg, amarsvg])

            plt.text(-1, 0.02, s='Disagree C', va='top', ha='center')
            plt.text(-1, 0.27, s='Disagree S', va='top', ha='center')
            plt.text(-1, 0.50, s='Neutral', va='top', ha='center')
            plt.text(-1, 0.76, s='Agree S', va='top', ha='center')
            plt.text(-1, 1, s='Agree C', va='top', ha='center')

            plt.text(0, 0, s='work tech', va='top', ha='center')
            plt.text(1, 1, s='notice improvements', va='bottom', ha='center')
            plt.text(2, 0, s='problem solving', va='top', ha='center')
            plt.text(3, 1, s='diversity', va='bottom', ha='center')
            plt.text(4, 0, s='adblocker', va='top', ha='center')
            plt.text(5, 1, s='alcohol', va='bottom', ha='center')
            plt.text(6, 0, s='love boss', va='top', ha='center')
            plt.text(7, 1, s='night coder', va='bottom', ha='center')
            plt.text(8, 0, s='legacy', va='top', ha='center')
            plt.text(9, 1, s='go to mars', va='bottom', ha='center')

            plt.plot([0, 0], [0, 1], color='k', lw=1)
            plt.plot([1, 1], [0, 1], color='k', lw=1)
            plt.plot([2, 2], [0, 1], color='k', lw=1)
            plt.plot([3, 3], [0, 1], color='k', lw=1)
            plt.plot([4, 4], [0, 1], color='k', lw=1)
            plt.plot([5, 5], [0, 1], color='k', lw=1)
            plt.plot([6, 6], [0, 1], color='k', lw=1)
            plt.plot([7, 7], [0, 1], color='k', lw=1)
            plt.plot([8, 8], [0, 1], color='k', lw=1)
            plt.plot([9, 9], [0, 1], color='k', lw=1)

            ax = plt.gca()
            ax.axis('off')

            plt.title("Agree or Disagree " + region + " Region")
            plt.savefig('imgs/AoD' + region + ".png")
            plt.show()
            plt.clf()

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'pink', 'brown', 'orange', 'gray', 'gold', 'lime']
    for i, c in zip(range(len(regionset)), colors):
        plt.plot([0, 1], [avglist[i][0], avglist[i][1]], color=c, lw=2, label=regionset[i])
        plt.plot([1, 2], [avglist[i][1], avglist[i][2]], color=c, lw=2)
        plt.plot([2, 3], [avglist[i][2], avglist[i][3]], color=c, lw=2)
        plt.plot([3, 4], [avglist[i][3], avglist[i][4]], color=c, lw=2)
        plt.plot([4, 5], [avglist[i][4], avglist[i][5]], color=c, lw=2)
        plt.plot([5, 6], [avglist[i][5], avglist[i][6]], color=c, lw=2)
        plt.plot([6, 7], [avglist[i][6], avglist[i][7]], color=c, lw=2)
        plt.plot([7, 8], [avglist[i][7], avglist[i][8]], color=c, lw=2)
        plt.plot([8, 9], [avglist[i][8], avglist[i][9]], color=c, lw=2)

    plt.text(-1, 0.02, s='Disagree C', va='top', ha='center')
    plt.text(-1, 0.27, s='Disagree S', va='top', ha='center')
    plt.text(-1, 0.50, s='Neutral', va='top', ha='center')
    plt.text(-1, 0.76, s='Agree S', va='top', ha='center')
    plt.text(-1, 1, s='Agree C', va='top', ha='center')
    plt.text(0, 0, s='work tech', va='top', ha='center')
    plt.text(1, 1, s='notice improvements', va='bottom', ha='center')
    plt.text(2, 0, s='problem solving', va='top', ha='center')
    plt.text(3, 1, s='diversity', va='bottom', ha='center')
    plt.text(4, 0, s='adblocker', va='top', ha='center')
    plt.text(5, 1, s='alcohol', va='bottom', ha='center')
    plt.text(6, 0, s='love boss', va='top', ha='center')
    plt.text(7, 1, s='night coder', va='bottom', ha='center')
    plt.text(8, 0, s='legacy', va='top', ha='center')
    plt.text(9, 1, s='go to mars', va='bottom', ha='center')

    plt.plot([0, 0], [0, 1], color='k', lw=1)
    plt.plot([1, 1], [0, 1], color='k', lw=1)
    plt.plot([2, 2], [0, 1], color='k', lw=1)
    plt.plot([3, 3], [0, 1], color='k', lw=1)
    plt.plot([4, 4], [0, 1], color='k', lw=1)
    plt.plot([5, 5], [0, 1], color='k', lw=1)
    plt.plot([6, 6], [0, 1], color='k', lw=1)
    plt.plot([7, 7], [0, 1], color='k', lw=1)
    plt.plot([8, 8], [0, 1], color='k', lw=1)
    plt.plot([9, 9], [0, 1], color='k', lw=1)

    ax = plt.gca()
    ax.axis('off')

    plt.title("Agree or Disagree Region Averages")
    plt.legend(loc=(0.06, 0.06))
    plt.savefig('imgs/AoD_avgs.png')
    plt.show()
    plt.clf()

def gender_salary():
    salaryset = set(salary)
    salaryset = sorted([x for x in salaryset if x == x])
    # print(salaryset)
    # df["gender"] =
    no_nan_df = df.dropna(subset=['gender', 'salary_midpoint', 'age_midpoint'])
    no_nan_df = no_nan_df[no_nan_df.gender != 'Prefer not to disclose']
    no_nan_df = no_nan_df[no_nan_df.gender != 'Other']
    female_salary_by_age = list(range(8))
    female_count_age = list(range(8))
    male_salary_by_age = list(range(8))
    male_count_age = list(range(8))
    male_experience_by_age = list(range(8))
    female_experience_by_age = list(range(8))
    # iterate through data and keep track of age, gender, counts to get average salary and average experience
    #   by age group and gender
    for index, rows in no_nan_df.iterrows():
        if rows['age_midpoint'] == 16:
            insert_i = 0
        if rows['age_midpoint'] == 22:
            insert_i = 1
        if rows['age_midpoint'] == 27:
            insert_i = 2
        if rows['age_midpoint'] == 32:
            insert_i = 3
        if rows['age_midpoint'] == 37:
            insert_i = 4
        if rows['age_midpoint'] == 44.5:
            insert_i = 5
        if rows['age_midpoint'] == 54.5:
            insert_i = 6
        if rows['age_midpoint'] == 65:
            insert_i = 7
        if rows['gender'] == 'Female':
            female_count_age[insert_i] +=1
            female_salary_by_age[insert_i] += rows['salary_midpoint']
            female_experience_by_age[insert_i] += rows['experience_midpoint']
        elif rows['gender'] == 'Male':
            male_count_age[insert_i] += 1
            male_salary_by_age[insert_i] += rows['salary_midpoint']
            male_experience_by_age[insert_i] += rows['experience_midpoint']

    average_male_salary = list(range(8))
    average_female_salary = list(range(8))
    average_male_experience = list(range(8))
    average_female_experience = list(range(8))
    for i in range(0, 7, 1):
        average_female_experience[i] = female_experience_by_age[i] / female_count_age[i]
        average_female_salary[i] = female_salary_by_age[i] / female_count_age[i]
        average_male_experience[i] = male_experience_by_age[i] / male_count_age[i]
        average_male_salary[i] = male_salary_by_age[i] / male_count_age[i]

    colors = {'Female Salary': 'hotpink', 'Female Exp': 'darkmagenta',
              'Male Salary': 'mediumturquoise', 'Male Exp': 'teal'}

    ax = plt.subplot(111)
    x = [16, 22, 27, 32, 37, 44.5, 54.5, 65]
    ax.bar(x, average_female_salary, color = 'hotpink')
    # plot = plot(x="experience_midpoint", y="age_midpoint", s=no_nan_df.salary_midpoint/100, c=no_nan_df.gender.apply(lambda x: colors[x]),
    #            kind='scatter', figsize = (7,7), title='Salary and Experience by Age')
    # plt.set_xlabel("experience")
    # plt.set_ylabel("age")
    plt.show()


def important():
    # choices = ['I don't care about this', 'This is somewhat important', 'This is very important']

    regionset = set(soregion)
    regionset = sorted([x for x in regionset if x == x])
    # regionset = ['Africa', 'Antarctica', 'Caribbean', 'Central America', 'Central Asia', 'East Asia',
    #  'Eastern Europe', 'Middle East', 'North America', 'Oceania', 'South America', 'South Asia',
    #  'Southeast Asia', 'Western Europe']

    avglist = []

    for region in regionset:
        indx = 0
        idxlist = []

        ivarietyavg = 0
        icontrolavg = 0
        isameendavg = 0
        inewtechavg = 0
        ibuildnewavg = 0
        ibuildexistingavg = 0
        ipromotionavg = 0
        imissionavg = 0
        iwfhavg = 0
        iofficeavh = 0

        for i in range(len(atech)):
            if len(idxlist) < 100:
                if type(ivariety[i]) is str and type(icontrol[i]) is str and type(isameend[i]) is str and \
                        type(inewtech[i]) is str and type(ibuildnew[i]) is str and type (ibuildexisting[i]) is str and \
                        type(ipromotion[i]) is str and type(imission[i]) is str and type(iwfh[i]) is str and type(ioffice[i]) is str:
                    idxlist.append(indx)
                    ivariety[i] = importancevalue(ivariety[i])
                    icontrol[i] = importancevalue(icontrol[i])
                    isameend[i] = importancevalue(isameend[i])
                    inewtech[i] = importancevalue(inewtech[i])
                    ibuildnew[i] = importancevalue(ibuildnew[i])
                    ibuildexisting[i] = importancevalue(ibuildexisting[i])
                    ipromotion[i] = importancevalue(ipromotion[i])
                    imission[i] = importancevalue(imission[i])
                    iwfh[i] = importancevalue(iwfh[i])
                    ioffice[i] = importancevalue(ioffice[i])

                    ivarietyavg += ivariety[i]
                    icontrolavg += icontrol[i]
                    isameendavg += isameend[i]
                    inewtechavg += inewtech[i]
                    ibuildnewavg += ibuildnew[i]
                    ibuildexistingavg += ibuildexisting[i]
                    ipromotionavg += ipromotion[i]
                    imissionavg += imission[i]
                    iwfhavg += iwfh[i]
                    iofficeavh += ioffice[i]

                indx += 1

        if len(idxlist) > 0:
            ivarietyavg /= len(idxlist)
            icontrolavg /= len(idxlist)
            isameendavg /= len(idxlist)
            inewtechavg /= len(idxlist)
            ibuildnewavg /= len(idxlist)
            ibuildexistingavg /= len(idxlist)
            ipromotionavg /= len(idxlist)
            imissionavg /= len(idxlist)
            iwfhavg /= len(idxlist)
            iofficeavh /= len(idxlist)

            plt.rcParams["figure.figsize"] = [10.0, 8.0]

            for i in idxlist:
                plt.plot([0, 1], [ivariety[i], icontrol[i]], color='c', lw=.3)
                plt.plot([1, 2], [icontrol[i], isameend[i]], color='c', lw=.3)
                plt.plot([2, 3], [isameend[i], inewtech[i]], color='c', lw=.3)
                plt.plot([3, 4], [inewtech[i], ibuildnew[i]], color='c', lw=.3)
                plt.plot([4, 5], [ibuildnew[i], ibuildexisting[i]], color='c', lw=.3)
                plt.plot([5, 6], [ibuildexisting[i], ipromotion[i]], color='c', lw=.3)
                plt.plot([6, 7], [ipromotion[i], imission[i]], color='c', lw=.3)
                plt.plot([7, 8], [imission[i], iwfh[i]], color='c', lw=.3)
                plt.plot([8, 9], [iwfh[i], ioffice[i]], color='c', lw=.3)

            plt.plot([0, 1], [ivarietyavg, icontrolavg], color='r', lw=2)
            plt.plot([1, 2], [icontrolavg, isameendavg], color='r', lw=2)
            plt.plot([2, 3], [isameendavg, inewtechavg], color='r', lw=2)
            plt.plot([3, 4], [inewtechavg, ibuildnewavg], color='r', lw=2)
            plt.plot([4, 5], [ibuildnewavg, ibuildexistingavg], color='r', lw=2)
            plt.plot([5, 6], [ibuildexistingavg, ipromotionavg], color='r', lw=2)
            plt.plot([6, 7], [ipromotionavg, imissionavg], color='r', lw=2)
            plt.plot([7, 8], [imissionavg, iwfhavg], color='r', lw=2)
            plt.plot([8, 9], [iwfhavg, iofficeavh], color='r', lw=2)

            avglist.append([ivarietyavg, icontrolavg, isameendavg, inewtechavg, ibuildnewavg, ibuildexistingavg, ipromotionavg,
                            imissionavg, iwfhavg, iofficeavh])

            plt.text(-1, 0.02, s="Don't Care", va='top', ha='center')
            plt.text(-1, 0.50, s='Somewhat Important', va='top', ha='center')
            plt.text(-1, 1, s='Very Important', va='top', ha='center')

            plt.text(0, 0, s='variety', va='top', ha='center')
            plt.text(1, 1, s='control', va='bottom', ha='center')
            plt.text(2, 0, s='same time', va='top', ha='center')
            plt.text(3, 1, s='new tech', va='bottom', ha='center')
            plt.text(4, 0, s='new build', va='top', ha='center')
            plt.text(5, 1, s='improve existing', va='bottom', ha='center')
            plt.text(6, 0, s='promoted', va='top', ha='center')
            plt.text(7, 1, s='mission', va='bottom', ha='center')
            plt.text(8, 0, s='from home', va='top', ha='center')
            plt.text(9, 1, s='own office', va='bottom', ha='center')

            plt.plot([0, 0], [0, 1], color='k', lw=1)
            plt.plot([1, 1], [0, 1], color='k', lw=1)
            plt.plot([2, 2], [0, 1], color='k', lw=1)
            plt.plot([3, 3], [0, 1], color='k', lw=1)
            plt.plot([4, 4], [0, 1], color='k', lw=1)
            plt.plot([5, 5], [0, 1], color='k', lw=1)
            plt.plot([6, 6], [0, 1], color='k', lw=1)
            plt.plot([7, 7], [0, 1], color='k', lw=1)
            plt.plot([8, 8], [0, 1], color='k', lw=1)
            plt.plot([9, 9], [0, 1], color='k', lw=1)

            ax = plt.gca()
            ax.axis('off')

            plt.title("Importance " + region + " Region")
            plt.savefig('imgs/I'+ region + ".png")
            plt.show()
            plt.clf()

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'pink', 'brown', 'orange', 'gray', 'gold', 'lime']
    for i, c in zip(range(len(regionset)), colors):
        plt.plot([0, 1], [avglist[i][0], avglist[i][1]], color=c, lw=2, label=regionset[i])
        plt.plot([1, 2], [avglist[i][1], avglist[i][2]], color=c, lw=2)
        plt.plot([2, 3], [avglist[i][2], avglist[i][3]], color=c, lw=2)
        plt.plot([3, 4], [avglist[i][3], avglist[i][4]], color=c, lw=2)
        plt.plot([4, 5], [avglist[i][4], avglist[i][5]], color=c, lw=2)
        plt.plot([5, 6], [avglist[i][5], avglist[i][6]], color=c, lw=2)
        plt.plot([6, 7], [avglist[i][6], avglist[i][7]], color=c, lw=2)
        plt.plot([7, 8], [avglist[i][7], avglist[i][8]], color=c, lw=2)
        plt.plot([8, 9], [avglist[i][8], avglist[i][9]], color=c, lw=2)

    plt.text(-1, 0.02, s="Don't Care", va='top', ha='center')
    plt.text(-1, 0.50, s='Somewhat Important', va='top', ha='center')
    plt.text(-1, 1, s='Very Important', va='top', ha='center')

    plt.text(0, 0, s='variety', va='top', ha='center')
    plt.text(1, 1, s='control', va='bottom', ha='center')
    plt.text(2, 0, s='same time', va='top', ha='center')
    plt.text(3, 1, s='new tech', va='bottom', ha='center')
    plt.text(4, 0, s='new build', va='top', ha='center')
    plt.text(5, 1, s='improve existing', va='bottom', ha='center')
    plt.text(6, 0, s='promoted', va='top', ha='center')
    plt.text(7, 1, s='mission', va='bottom', ha='center')
    plt.text(8, 0, s='from home', va='top', ha='center')
    plt.text(9, 1, s='own office', va='bottom', ha='center')

    plt.plot([0, 0], [0, 1], color='k', lw=1)
    plt.plot([1, 1], [0, 1], color='k', lw=1)
    plt.plot([2, 2], [0, 1], color='k', lw=1)
    plt.plot([3, 3], [0, 1], color='k', lw=1)
    plt.plot([4, 4], [0, 1], color='k', lw=1)
    plt.plot([5, 5], [0, 1], color='k', lw=1)
    plt.plot([6, 6], [0, 1], color='k', lw=1)
    plt.plot([7, 7], [0, 1], color='k', lw=1)
    plt.plot([8, 8], [0, 1], color='k', lw=1)
    plt.plot([9, 9], [0, 1], color='k', lw=1)

    ax = plt.gca()
    ax.axis('off')

    plt.title("Importance Region Averages")
    plt.legend(loc=(0.35, 0.06))
    plt.savefig('imgs/I_avgs.png')
    plt.show()
    plt.clf()



def main():
    # agree()
    # important()
    print("hello")
    # setvar = set(atech)
    # setvar = sorted([x for x in setvar if x == x])
    # print(setvar)


if __name__ == '__main__':
    main()

