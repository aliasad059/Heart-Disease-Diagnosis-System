output_membership = {
    'healthy': 0.,
    'sick_1': 0.,
    'sick_2': 0.,
    'sick_3': 0.,
    'sick_4': 0.
}


def infer_healthy_membership(inputs_membership):
    """
        checks rules for healthy.

        Healthy rules are:
            RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
            RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
            RULE 23: IF (cholesterol IS low) THEN health IS healthy;
            RULE 29: IF (ecg IS normal) THEN health IS healthy;
            RULE 34: IF (heart_rate IS low) THEN health IS healthy;
            RULE 40: IF (old_peak IS low) THEN health IS healthy;
            RULE 45: IF (thallium_scan IS normal) THEN health IS healthy;
            RULE 50: IF (age IS young) THEN health IS healthy;
    """
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['chest_pain'] == 1)
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['blood_pressure'][0])
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['cholesterol'][0])
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['ecg'][0])
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['heart_rate'][0])
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['old_peak'][0])
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['thallium_scan'] == 3)
    output_membership['healthy'] = max(output_membership['healthy'], inputs_membership['age'][0])
    return output_membership['healthy']


def infer_sick_1_membership(inputs_membership):
    """
        checks rules for sick_1.

        Sick_1 rules are:
            RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
            RULE 10: IF (blood_pressure IS high) OR (heart_rate IS low) THEN health IS sick_1;
            RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
            RULE 16: IF (sex IS female) THEN health IS sick_1;
            RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
            RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;
            RULE 30: IF (ecg IS normal) THEN health IS sick_1;
            RULE 35: IF (heart_rate IS medium) THEN health IS sick_1;
            RULE 41: IF (old_peak IS low) THEN health IS sick_1;
            RULE 46: IF (thallium_scan IS normal) THEN health IS sick_1;
            RULE 51: IF (age IS mild) THEN health IS sick_1;
    """
    output_membership['sick_1'] = max(output_membership['sick_1'],
                                      max(inputs_membership['chest_pain'] == 4, inputs_membership['age'][3]))
    output_membership['sick_1'] = max(output_membership['sick_1'],
                                      max(inputs_membership['blood_pressure'][2], inputs_membership['heart_rate'][0]))
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['chest_pain'] == 2)
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['sex'] == 2)
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['blood_pressure'][1])
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['cholesterol'][1])
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['ecg'][0])
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['heart_rate'][1])
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['old_peak'][0])
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['thallium_scan'] == 3)
    output_membership['sick_1'] = max(output_membership['sick_1'], inputs_membership['age'][1])
    return output_membership['sick_1']


def infer_sick_2_membership(inputs_membership):
    """
        checks rules for sick_2.

        Sick_2 rules are:
            RULE 4: IF (sex IS female) AND (heart_rate IS medium) THEN health IS sick_2;
            RULE 6: IF (chest_pain IS typical_anginal) AND (heart_rate IS medium) THEN health IS sick_2;
            RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
            RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;
            RULE 17: IF (sex IS male) THEN health IS sick_2;
            RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
            RULE 25: IF (cholesterol IS high) THEN health IS sick_2;
            RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
            RULE 31: IF (ecg IS abnormal) THEN health IS sick_2;
            RULE 36: IF (heart_rate IS medium) THEN health IS sick_2;
            RULE 39: IF (exercise IS true) THEN health IS sick_2;
            RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
            RULE 47: IF (thallium_scan IS medium) THEN health IS sick_2;
            RULE 52: IF (age IS old) THEN health IS sick_2;
    """
    output_membership['sick_2'] = max(output_membership['sick_2'],
                                      min(inputs_membership['sex'] == 2, inputs_membership['heart_rate'][1]))
    output_membership['sick_2'] = max(output_membership['sick_2'],
                                      min(inputs_membership['chest_pain'] == 1, inputs_membership['heart_rate'][1]))
    if inputs_membership['blood_sugar'] < 1:
        output_membership['sick_2'] = max(output_membership['sick_2'],
                                          min(inputs_membership['blood_sugar'], inputs_membership['blood_pressure'][3]))
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['chest_pain'] == 3)
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['sex'] == 1)
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['blood_pressure'][2])
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['cholesterol'][2])
    if inputs_membership['blood_sugar'] == 1:
        output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['blood_sugar'])
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['ecg'][1])
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['heart_rate'][1])
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['exercise'])
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['old_peak'][2])
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['thallium_scan'] == 6)
    output_membership['sick_2'] = max(output_membership['sick_2'], inputs_membership['age'][2])

    return output_membership['sick_2']


def infer_sick_3_membership(inputs_membership):
    """
        checks rules for sick_3.

        Sick_3 rules are:
            RULE 3: IF (sex IS male) AND (heart_rate IS medium) THEN health IS sick_3;
            RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
            RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
            RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
            RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
            RULE 26: IF (cholesterol IS high) THEN health IS sick_3;
            RULE 32: IF (ecg IS hypertrophy) THEN health IS sick_3;
            RULE 37: IF (heart_rate IS high) THEN health IS sick_3;
            RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
            RULE 48: IF (thallium_scan IS high) THEN health IS sick_3;
            RULE 53: IF (age IS old) THEN health IS sick_3;
    """
    output_membership['sick_3'] = max(output_membership['sick_3'],
                                      min(inputs_membership['sex'] == 1, inputs_membership['heart_rate'][1]))
    output_membership['sick_3'] = max(output_membership['sick_3'],
                                      min(inputs_membership['chest_pain'] == 3, inputs_membership['blood_pressure'][2]))
    if inputs_membership['blood_sugar'] == 1:
        output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['age'][1])
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['chest_pain'] == 4)
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['blood_pressure'][2])
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['cholesterol'][2])
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['ecg'][2])
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['heart_rate'][2])
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['old_peak'][2])
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['thallium_scan'] == 7)
    output_membership['sick_3'] = max(output_membership['sick_3'], inputs_membership['age'][2])

    return output_membership['sick_3']


def infer_sick_4_membership(inputs_membership):
    """
        checks rules for sick_4.

        Sick_4 rules are:
            RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;
            RULE 2: IF (heart_rate IS high) AND (age IS old) THEN health IS sick_4;
            RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
            RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
            RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;
            RULE 33: IF (ecg IS hypertrophy) THEN health IS sick_4;
            RULE 38: IF (heart_rate IS high) THEN health IS sick_4;
            RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
            RULE 49: IF (thallium_scan IS high) THEN health IS sick_4;
            RULE 54: IF (age IS very_old) THEN health IS sick_4;
    """
    output_membership['sick_4'] = max(output_membership['sick_4'],
                                      min(inputs_membership['age'][3], inputs_membership['chest_pain'] == 2))
    output_membership['sick_4'] = max(output_membership['sick_4'],
                                      min(inputs_membership['heart_rate'][2], inputs_membership['age'][2]))
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['chest_pain'] == 4)
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['blood_pressure'][3])
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['cholesterol'][3])
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['ecg'][2])
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['heart_rate'][2])
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['old_peak'][1])
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['thallium_scan'] == 7)
    output_membership['sick_4'] = max(output_membership['sick_4'], inputs_membership['age'][3])

    return output_membership['sick_4']


def infer_memberships(fuzzified_inputs):
    """
        infer the membership of each variable.

        Args:
            fuzzified_inputs: a dictionary of fuzzified inputs.
    """
    infer_healthy_membership(fuzzified_inputs)
    infer_sick_1_membership(fuzzified_inputs)
    infer_sick_2_membership(fuzzified_inputs)
    infer_sick_3_membership(fuzzified_inputs)
    infer_sick_4_membership(fuzzified_inputs)

    return output_membership
