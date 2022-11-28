#!/bin/env python3

import sys

def candidate_key(c1):
    return c1['sml']

if __name__ == "__main__":
    # Inputs
    preference_db = sys.argv[1]
    vacancy_db = sys.argv[2]

    # Scan Candidate preferences
    candidates = []
    with open(preference_db) as f:
        for line in f.readlines():    
            if line.startswith('#'): continue

            tuples = line.split(',') 

            record = {}
            record['name'] = tuples[0].strip()
            record['id'] = tuples[1].strip()
            record['percentile'] = tuples[2].strip()
            record['sml'] = int(tuples[3].strip())
            record['preferences'] = tuples[4].strip().split(':')

            candidates.append(record)

    candidates.sort(key=lambda x:x['sml'])
    print("Candidates: \n", candidates)

    # Scan Vacancies
    vacancies = {}
    with open(vacancy_db) as f:
        for line in f.readlines():
            if line.startswith('#'): continue
            tuples = line.split(',')
            vacancies[tuples[0].strip()] = int(tuples[1].strip())

    print("Vacancies: \n", vacancies)

    # Perform Allotment
    allotment = {}  # output
    for c in candidates:
        for preference in c['preferences']:
            if vacancies[preference] > 0:
                vacancies[preference] -= 1
                allotment[c['name']] = preference
                break

    print("Alottment: \n", allotment)

