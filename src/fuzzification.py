def get_membership_function(p1, p2, p3):
    """
    Returns a function that returns the miu value of a given input. (assumes that the membership relations are linear)
    :param p1: first point of the function
    :param p2: second point of the function
    :param p3: third point of the function
    :return: membership function of the input
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    def miu_function(x):
        if x <= x1:
            return y1
        elif x <= x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        elif x <= x3:
            return y2 + (y3 - y2) * (x - x2) / (x3 - x2)
        else:
            return y3

    return miu_function


age_young_miu = get_membership_function((0, 1), (29, 1), (38, 0))
age_mild_miu = get_membership_function((33, 0), (38, 1), (45, 0))
age_old_miu = get_membership_function((40, 0), (48, 1), (58, 0))
age_veryOld_miu = get_membership_function((0, 0), (52, 0), (60, 1))


def age_fuzzification(age):
    return [
        age_young_miu(age),
        age_mild_miu(age),
        age_old_miu(age),
        age_veryOld_miu(age)
    ]


blood_pressure_low_miu = get_membership_function((0, 1), (111, 1), (134, 0))
blood_pressure_medium_miu = get_membership_function((127, 0), (139, 1), (153, 0))
blood_pressure_high_miu = get_membership_function((142, 0), (157, 1), (172, 0))
blood_pressure_veryHigh_miu = get_membership_function((0, 0), (154, 0), (171, 1))


def blood_pressure_fuzzification(blood_pressure):
    return [
        blood_pressure_low_miu(blood_pressure),
        blood_pressure_medium_miu(blood_pressure),
        blood_pressure_high_miu(blood_pressure),
        blood_pressure_veryHigh_miu(blood_pressure)
    ]


blood_sugar_miu = get_membership_function((0, 0), (105, 0), (120, 1))


def blood_sugar_fuzzification(blood_sugar):
    return [
        blood_sugar_miu(blood_sugar)
    ]


cholesterol_low_miu = get_membership_function((0, 1), (151, 1), (197, 0))
cholesterol_medium_miu = get_membership_function((188, 0), (215, 1), (250, 0))
cholesterol_high_miu = get_membership_function((217, 0), (263, 1), (307, 0))
cholesterol_veryHigh_miu = get_membership_function((0, 0), (281, 0), (347, 1))


def cholesterol_fuzzification(cholesterol):
    return [
        cholesterol_low_miu(cholesterol),
        cholesterol_medium_miu(cholesterol),
        cholesterol_high_miu(cholesterol),
        cholesterol_veryHigh_miu(cholesterol)
    ]


heart_rate_low_miu = get_membership_function((0, 1), (100, 1), (141, 0))
heart_rate_medium_miu = get_membership_function((111, 0), (152, 1), (194, 0))
heart_rate_high_miu = get_membership_function((0, 0), (152, 0), (210, 1))


def heart_rate_fuzzification(heart_rate):
    return [
        heart_rate_low_miu(heart_rate),
        heart_rate_medium_miu(heart_rate),
        heart_rate_high_miu(heart_rate)
    ]


ECG_normal_miu = get_membership_function((0, 1), (0, 1), (0.4, 0))
ECG_abnormal_miu = get_membership_function((0.2, 0), (1, 1), (1.8, 0))
ECG_hypertrophy_miu = get_membership_function((0, 0), (1.4, 0), (1.9, 1))


def ECG_fuzzification(ECG):
    return [
        ECG_normal_miu(ECG),
        ECG_abnormal_miu(ECG),
        ECG_hypertrophy_miu(ECG)
    ]


old_peak_low_miu = get_membership_function((0, 1), (1, 1), (2, 0))
old_peak_risk_miu = get_membership_function((1.5, 0), (2.8, 1), (4.2, 0))
old_peak_terrible_miu = get_membership_function((0, 0), (2.5, 0), (4.2, 0))


def old_peak_fuzzification(old_peak):
    return [
        old_peak_low_miu(old_peak),
        old_peak_risk_miu(old_peak),
        old_peak_terrible_miu(old_peak)
    ]


output_healthy_miu = get_membership_function((0, 1), (0.25, 1), (1, 0))
output_s1_miu = get_membership_function((0, 0), (1, 1), (2, 0))
output_s2_miu = get_membership_function((1, 0), (2, 1), (3, 0))
output_s3_miu = get_membership_function((2, 0), (3, 1), (4, 0))
output_s4_miu = get_membership_function((0, 0), (3, 0), (3.75, 1))


def output_fuzzification(output):
    return [
        output_healthy_miu(output),
        output_s1_miu(output),
        output_s2_miu(output),
        output_s3_miu(output),
        output_s4_miu(output)
    ]
