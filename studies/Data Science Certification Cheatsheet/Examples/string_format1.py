'''
Created on Jun 28, 2017

@author: SummitWorks
'''
applicant = input("Enter the applicant's name: ")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time: ")
print(interviewer + ' will interview ' + applicant + ' at ' + time +'.')
print(interviewer, ' will interview ', applicant, ' at ', time, '.', sep='')
print('{} will interview {} at {}.'.format(interviewer, applicant, time))