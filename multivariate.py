import numpy as np
import pandas as pd

def main():
    # df = pd.read_csv('data/2016 Stack Overflow Survey Responses.csv')
    # print(df)
    # pd.to_pickle(df, 'data/SOpickle')

    df = pd.read_pickle('data/SOpickle')
    print(list(df))
    country = df['country']
    age = df['age_midpoint']
    gender = df['gender']
    occupation = df['occupation']
    experience = df['experience_midpoint']
    salary = df['salary_midpoint']
    aliens = df['aliens']
    ability = df['programming_ability']
    status = df['employment_status']
    industry = df['industry']
    companysize = df['company_size_range']
    teamsize = df['team_size_range']
    women = df['women_on_team']
    remote = df['remote']
    jobsatisfaction = df['job_satisfaction']
    pet = df['dogs_vs_cats']
    education = df['education']
    star = df['star_wars_vs_star_trek']
    atech = df['agree_tech']
    anotice = df['agree_notice']
    aproblem = df['agree_problemsolving']
    adiversity = df['agree_diversity']
    aadblocker = df['agree_adblocker']
    aalcohol = df['agree_alcohol']
    aboss = df['agree_loveboss']
    anight = df['agree_nightcode']
    alegacy = df['agree_legacy']
    amars = df['agree_mars']
    ivariety = df['important_variety']
    icontrol = df['important_control']
    isameend = df['important_sameend']
    inewtech = df['important_newtech']
    ibuildnew = df['important_buildnew']
    ibuildexisting = df['important_buildexisting']
    ipromotion = df['important_promotion']
    imission = df['important_companymission']
    iwfh = df['important_wfh']
    ioffice = df['important_ownoffice']
    challenges = df['developer_challenges']
    whystack = df['why_stack_overflow']
    interview = df['how_to_improve_interview_process']
    jobsearch = df['job_search_annoyance']
    newjob = df['open_to_new_job']
    jobvalue = df['new_job_value']

if __name__ == '__main__':
    main()

