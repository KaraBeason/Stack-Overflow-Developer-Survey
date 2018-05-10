import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

import random

import math

df = pd.read_csv('data/2016 Stack Overflow Survey Responses.csv')
age = np.array(df['age_midpoint'].data)

# print(df)
pd.to_pickle(df, 'data/SOpickle')

df = pd.read_pickle('data/SOpickle')

#  CUSTOM COLOR MAP that looks cool but obfuscates the message of the data.
# def make_colormap(seq):
#     """Return a LinearSegmentedColormap
#     seq: a sequence of floats and RGB-tuples. The floats should be increasing
#     and in the interval (0,1).
#     """
#     seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
#     cdict = {'red': [], 'green': [], 'blue': []}
#     for i, item in enumerate(seq):
#         if isinstance(item, float):
#             r1, g1, b1 = seq[i - 1]
#             r2, g2, b2 = seq[i + 1]
#             cdict['red'].append([item, r1, r2])
#             cdict['green'].append([item, g1, g2])
#             cdict['blue'].append([item, b1, b2])
#
#     return mcolors.LinearSegmentedColormap('CustomMap', cdict)
#
#
# c = mcolors.ColorConverter().to_rgb
# rvb_f = make_colormap(
#     [c('indigo'), 0.125, c('indigo'), c('darkmagenta'), 0.25, c('darkmagenta'), c('orchid'), 0.5, c('orchid'),
#      0.7, c('hotpink'), c('hotpink'), 0.75, c('lightpink')])
# rvb_m = make_colormap(
#     [c('midnightblue'), 0.125, c('midnightblue'), c('teal'), 0.25, c('teal'), c('mediumturquoise'), 0.5, c('mediumspringgreen'),
#      0.7, c('mediumspringgreen'), c('skyblue'), 0.75, c('skyblue')])

def gender_salary():
    ageset = set(age)
    ageset = sorted([x for x in ageset if x == x])

    no_nan_df = df.dropna(subset=['gender', 'salary_midpoint', 'age_midpoint', 'experience_midpoint', 'industry'])
    no_nan_df = no_nan_df[no_nan_df.gender != 'Prefer not to disclose']
    no_nan_df = no_nan_df[no_nan_df.gender != 'Other']
    female_salary_by_age = list(range(8))
    female_count_age = list(range(8))
    male_salary_by_age = list(range(8))
    male_count_age = list(range(8))
    male_experience_by_age = list(range(8))
    female_experience_by_age = list(range(8))

    industries_set = no_nan_df.industry.values
    female_industry_by_age = dict.fromkeys(set(industries_set), 0)
    male_industry_by_age = dict.fromkeys(set(industries_set), 0)
    female_industry_salary = dict.fromkeys(set(industries_set), 0)
    male_industry_salary = dict.fromkeys(set(industries_set), 0)

    # dictionaries excluding "software products" industry that skews data set
    male_ind_exclude_gen = dict.fromkeys((set(industries_set)), 0)
    del male_ind_exclude_gen['Software Products']
    female_ind_exclude_gen = dict.fromkeys((set(industries_set)), 0)
    del female_ind_exclude_gen['Software Products']

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
            female_count_age[insert_i] += 1
            female_salary_by_age[insert_i] += rows['salary_midpoint']
            female_experience_by_age[insert_i] += rows['experience_midpoint']
            female_industry_by_age[rows['industry']] += 1
            female_industry_salary[rows['industry']] += rows['salary_midpoint']
            # if rows['industry'] is not 'Software Products':
            #     female_ind_exclude_gen[rows['industry']] += 1
        elif rows['gender'] == 'Male':
            male_count_age[insert_i] += 1
            male_salary_by_age[insert_i] += rows['salary_midpoint']
            male_experience_by_age[insert_i] += rows['experience_midpoint']
            male_industry_by_age[rows['industry']] += 1
            male_industry_salary[rows['industry']] += rows['salary_midpoint']
            # if rows['industry'] is not 'Software Products':
            #     female_ind_exclude_gen[rows['industry']] += 1
    average_male_salary = list(range(8))
    average_female_salary = list(range(8))
    average_male_experience = list(range(8))
    average_female_experience = list(range(8))

    for i in range(0, 8, 1):
        average_female_experience[i] = female_experience_by_age[i] / female_count_age[i]
        average_female_salary[i] = female_salary_by_age[i] / female_count_age[i]
        average_male_experience[i] = male_experience_by_age[i] / male_count_age[i]
        average_male_salary[i] = male_salary_by_age[i] / male_count_age[i]
    plt.figure(0)
    ax = plt.subplot(111)
    ax2 = ax.twinx()
    x = [16, 22, 27, 32, 37, 44.5, 54.5, 65]
    for i in range(0, 8, 1):
        ax.bar(x[i] - 1.5, average_female_salary[i], color='hotpink')
        ax.bar(x[i] - .5, average_male_salary[i], color='mediumturquoise')
        ax2.bar(x[i] + .5, average_female_experience[i], color='darkmagenta')
        ax2.bar(x[i] + 1.5, average_male_experience[i], color='teal')
    ax.set_xlabel("Age Midpoint")
    ax.set_ylabel("Average Salary in USD")
    ax2.set_ylabel("Average Experience")
    handles = []
    fem_sal = mpatches.Patch(color='hotpink', label='Female Salary')
    handles.append(fem_sal)
    male_sal = mpatches.Patch(color='mediumturquoise', label='Male Salary')
    handles.append(male_sal)
    fem_exp = mpatches.Patch(color='darkmagenta', label='Female Experience')
    handles.append(fem_exp)
    male_exp = mpatches.Patch(color='teal', label='Male Experience')
    handles.append(male_exp)
    plt.legend(handles=handles)
    plt.xticks(ageset)
    plt.tight_layout()
    plt.savefig("Average Salary and Experience by Gender and Age Group.png")

    # get average salary by industry
    avg_female_salary_industry = dict(
        (k, float(female_industry_salary[k]) / female_industry_by_age[k]) for k in female_industry_salary)
    avg_male_salary_industry = dict(
        (k, float(male_industry_salary[k]) / male_industry_by_age[k]) for k in male_industry_salary)

    fig2 = plt.figure(1)
    ax4 = plt.subplot(111)
    ax3 = ax4.twinx()
    print(female_industry_by_age.values())
    x = np.arange(0, len(female_industry_by_age), 1)
    x = np.multiply(x, 5)
    N = len(female_industry_by_age)
    ax4.set_xlabel("Industry")
    ax4.set_ylabel("Average Salary in USD")
    ax3.set_ylabel("Number of Participants")
    ax3.bar(x - 1.25, list(female_industry_by_age.values()), align='center', width=.5, color= 'violet')
    ax4.bar(x - .5, list(avg_female_salary_industry.values()), align='center', width=.5, color='deeppink')
    ax3.bar(x + .5, list(male_industry_by_age.values()), align='center', width=.5, color='c')
    ax4.bar(x + 1.25, list(avg_male_salary_industry.values()), align='center', width=.5, color='darkcyan')
    # plt.tight_layout()

    ax4.set_xticks(x)
    ax4.set_xticklabels(list(female_industry_by_age.keys()), rotation='vertical')
    # plt.savefig("Average Salary and Number of Participants by Industry.png")
    handles = []
    fem_ind = mpatches.Patch(color='violet', label='Fem Industry')
    handles.append(fem_ind)
    male_ind = mpatches.Patch(color='c', label='Male Industry')
    handles.append(male_ind)
    fem_exp = mpatches.Patch(color='deeppink', label='Female Salary')
    handles.append(fem_exp)
    male_exp = mpatches.Patch(color='darkcyan', label='Male Salary')
    handles.append(male_exp)
    plt.legend(handles=handles)
    plt.tight_layout()
    # plt.axis('equal')
    # plt.show()
    plt.savefig("Average Salary by Industry and Gender.png")

    # **** the reported participation by males in "Software Products"
    # skews the data.  Adding a viz that excludes this "catchall" term.

    del avg_female_salary_industry['Software Products']
    del avg_male_salary_industry['Software Products']
    del female_industry_by_age['Software Products']
    del male_industry_by_age['Software Products']


    fig3 = plt.figure(2)
    ax5 = plt.subplot(111)
    ax6 = ax5.twinx()
    # print(female_industry_by_age.values())
    # x = np.arange(0, len(female_industry_by_age), 1)
    # x = np.multiply(x, 5)
    ax5.set_xlabel("Industry")
    ax5.set_ylabel("Average Salary in USD")
    ax6.set_ylabel("Number of Participants")
    x = np.arange(0, len(female_ind_exclude_gen), 1)
    x = np.multiply(x, 5)
    ax5.set_xticks(x)
    ax5.set_xticklabels(list(female_ind_exclude_gen.keys()), rotation='vertical')
    ax6.bar(x - 1.25, list(female_industry_by_age.values()), align='center', color= 'violet')
    ax5.bar(x - .4, list(avg_female_salary_industry.values()), align='center', color='deeppink')
    ax6.bar(x + .5, list(male_industry_by_age.values()), align='center', color='c')
    ax5.bar(x + 1.26, list(avg_male_salary_industry.values()), align='center', color='darkcyan')
    # plt.tight_layout()
    handles = []
    fem_ind = mpatches.Patch(color='violet', label='Fem Industry')
    handles.append(fem_ind)
    male_ind = mpatches.Patch(color='c', label='Male Industry')
    handles.append(male_ind)
    fem_exp = mpatches.Patch(color='deeppink', label='Female Salary')
    handles.append(fem_exp)
    male_exp = mpatches.Patch(color='darkcyan', label='Male Salary')
    handles.append(male_exp)
    plt.legend(handles=handles)
    # plt.show()

    plt.savefig("Average Salary by Industry Excluding Software Products.png")


def main():
    gender_salary()



if __name__ == '__main__':
    main()
