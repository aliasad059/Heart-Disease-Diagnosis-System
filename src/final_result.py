from fuzzification import fuzzify
from defuzzification import defuzzify
from inference import infer_memberships


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        fuzzified_input = fuzzify(input_dict)
        inferred_memberships = infer_memberships(fuzzified_input)
        defuzzified_output = defuzzify(inferred_memberships)
        output = ''
        if defuzzified_output < 1.78:
            output += 'healthy & '
        if 1 < defuzzified_output <= 2.51:
            output += 'sick1 & '
        if 1.78 < defuzzified_output <= 3.25:
            output += 'sick2 & '
        if 1.5 < defuzzified_output <= 4.5:
            output += 'sick3 & '
        if defuzzified_output > 3.25:
            output += 'sick4 & '
        return output[:-3] + ' : ' + str(round(defuzzified_output, 2))
