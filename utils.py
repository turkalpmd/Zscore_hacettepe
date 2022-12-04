

import pandas as pd


from pygrowup import Calculator
#from pygrowup import helpers


def calc(weight,height,age,gender):

    if age <= 24:
        calculator = Calculator(adjust_height_data=False, 
                                adjust_weight_scores=False,
                                include_cdc=False, 
                                logger_name='pygrowup',
                                log_level='INFO')

        wfa = calculator.wfa(weight,age,gender)
        lhfa = calculator.lhfa(height,age,gender)

    if age > 24:
        calculator = Calculator(adjust_height_data=False, 
                                adjust_weight_scores=False,
                                include_cdc=True, 
                                logger_name='pygrowup',
                                log_level='INFO')

        wfa = calculator.wfa(weight,age,gender)
        lhfa = calculator.lhfa(height,age,gender)

    return wfa,lhfa
