# class tdcs_choose_feature:
#     def __init__(self,
#                  accelerated_learning,
#                  depression_and_anxiety,
#                  chronic_pain,
#                  reduced_addictive_cravings,
#                  imp_motor_skills_learning,
#                  improved_insight,
#                  reduced_risk_taking,
#                  increased_present_awareness,
#                  math,
#                  pitch_perception,
#                  improved_attention,
#                  memory_learning,
#                  alternate_depression_treatment,
#                  improved_socialization
#                  ):  # constructor
#
#         self.accelerated_learning = str(input(f'Input "1 and Enter" if need Accelerated Learning: ')).lower()
#         self.depression_and_anxiety = str(input(f'Input "2 and Enter" if need Depression and Anxiety: ')).lower()
#         self.chronic_pain = str(input(f'Input "3 and Enter" if need Chronic Pain: ')).lower()
#         self.reduced_addictive_cravings = str(
#             input(f'Input "4 and Enter" if need Reduced Addictive Cravings: ')).lower()
#         self.imp_motor_skills_learning = str(
#             input(f'Input "5 and Enter" if need Improved Motor Skills and Learning: ')).lower()
#         self.improved_insight = str(input(f'Input "6 and Enter" if need Improved Improved Insight: ')).lower()
#         self.reduced_risk_taking = str(input(f'Input "7 and Enter" if need Reduced Risk Taking: ')).lower()
#         self.increased_present_awareness = str(
#             input(f'Input "8 and Enter" if need Increased Present Awareness: ')).lower()
#         self.math = str(input(f'Input "9 and Enter" need Improved Mathematical Abilities:')).lower()
#         self.pitch_perception = str(input(f'Input "10 and Enter" need Pitch Perception:')).lower()
#         self.improved_attention = str(input(f'Input "11 and Enter" need Improved Attention:')).lower()
#         self.memory_learning = str(input(f'Input "12 and Enter" if need Memorization and Learning: ')).lower()
#         self.alternate_depression_treatment = str(
#             input(f'Input "13 and Enter" if need Alternate Depression Treatment: ')).lower()
#         self.improved_socialization = str(input(f'Input "14 and Enter" if need Improved Socialization: ')).lower()
#
#     def accel_learn(self):
#         if '1' in self.accelerated_learning:
#             print(
#                 '\nFor Accelerated Learning click: https://totaltdcs.com/electrode-placement-montage-list/accelerated-learning-darpa-montage/')
#         else:
#             print('\nYou did not choose Accelerated Learning')
#
#     def depress_and_anxiety(self):
#         if '2' in self.depression_and_anxiety:
#             print('For Depression and Anxiety: https://totaltdcs.com/electrode-placement-montage-list/depression-and-anxiety/')
#         else:
#             print('\nYou did not choose Depression and Anxiety')
#
#     def chron_pain(self):
#         if '3' in self.chronic_pain:
#             print('For Chronic Pain cick: https://totaltdcs.com/electrode-placement-montage-list/chronic-pain/')
#         else:
#             print('\nYou did not choose Chronic Pain')
#
#     def reduc_addictive_cravings(self):
#         if '4' in self.reduced_addictive_cravings:
#             print('For Reduced Addictive Cravings click: https://totaltdcs.com/electrode-placement-montage-list/cravings-and-addictions/')
#         else:
#             print('\nYou did not choose Reduced Addictive Cravings')
#
#     def imp_mot_sk_learning(self):
#         if '5' in self.imp_motor_skills_learning:
#             print('For Improved Motor Skills and Learning click: https://totaltdcs.com/electrode-placement-montage-list/improved-motor-skills-learning/')
#         else:
#             print('\nYou did not choose Improved Motor Skills and Learning')
#
#     def impr_insight(self):
#         if '6' in self.improved_insight:
#             print('For Improved Insight click: https://totaltdcs.com/electrode-placement-montage-list/improved-insight/')
#         else:
#             print('\nYou did not choose Improved Insight')
#
#     def reduc_risk_taking(self):
#         if '7' in self.reduced_risk_taking:
#             print('For Reduced Risk Taking click: https://totaltdcs.com/electrode-placement-montage-list/reduced-risk-taking/')
#         else:
#             print('\nYou did not choose Reduced Risk Taking')
#
#     def incr_present_awareness(self):
#         if '8' in self.increased_present_awareness:
#             print('For Increased Present Awareness click: https://totaltdcs.com/electrode-placement-montage-list/increased-present-awareness/')
#         else:
#             print('\nYou did not choose Increased Present Awareness')
#
#     def mathem(self):
#         if '9' in self.math:
#             print('For Improved Mathematical Abilities click: https://totaltdcs.com/electrode-placement-montage-list/improved-mathematical-abilities/')
#         else:
#             print('\nYou did not choose Improved Mathematical Abilities')
#
#     def pitch_percep(self):
#         if '10' in self.pitch_perception:
#             print('For Pitch Perception click: https://totaltdcs.com/electrode-placement-montage-list/pitch-perception/')
#         else:
#             print('\nYou did not choose Pitch Perception')
#
#     def impr_attention(self):
#         if '11' in self.improved_attention:
#             print('For Improved Attention click: https://totaltdcs.com/electrode-placement-montage-list/improved-attention/')
#         else:
#             print('\nYou did not choose Improved Attention')
#
#     def mem_learning(self):
#         if '12' in self.memory_learning:
#             print('For Memorization and Learning click: https://totaltdcs.com/electrode-placement-montage-list/memorization-and-learning/')
#         else:
#             print('\nYou did not choose Memorization and Learning')
#
#     def alter_depression_treatment(self):
#         if '13' in self.alternate_depression_treatment:
#             print('For Alternate Depression Treatment click: https://totaltdcs.com/electrode-placement-montage-list/alternative-depression-treatment/')
#         else:
#             print('\nYou did not choose Alternate Depression Treatment')
#
#     def impr_socialization(self):
#         if '14' in self.improved_socialization:
#             print('For Improved Socialization click: https://totaltdcs.com/electrode-placement-montage-list/improved-socialization/\n')
#         else:
#             print('\nYou did not choose Improved Socialization')
#
#
# tdcs_1 = tdcs_choose_feature('', '', '', '', '', '', '', '', '', '', '', '', '', '')
# tdcs_1.accel_learn()  # 1
# tdcs_1.depress_and_anxiety()  # 2
# tdcs_1.chron_pain()  # 3
# tdcs_1.reduc_addictive_cravings()  # 4
# tdcs_1.imp_mot_sk_learning()  # 5
# tdcs_1.impr_insight()  # 6
# tdcs_1.reduc_risk_taking()  # 7
# tdcs_1.incr_present_awareness()  # 8
# tdcs_1.mathem()  # 9
# tdcs_1.pitch_percep()  # 10
# tdcs_1.impr_attention()  # 11
# tdcs_1.mem_learning()  # 12
# tdcs_1.alter_depression_treatment()  # 13
# tdcs_1.impr_socialization()  # 14

from selenium import webdriver

class tdcs_choose_feature:
    def __init__(self,
                 accelerated_learning,
                 depression_and_anxiety,
                 chronic_pain,
                 reduced_addictive_cravings,
                 imp_motor_skills_learning,
                 improved_insight,
                 reduced_risk_taking,
                 increased_present_awareness,
                 math,
                 pitch_perception,
                 improved_attention,
                 memory_learning,
                 alternate_depression_treatment,
                 improved_socialization
                 ):  # constructor

        self.accelerated_learning = str(input(f'Input "1 and Enter" if need Accelerated Learning or type "exit": ')).lower()
        self.depression_and_anxiety = str(input(f'Input "2 and Enter" if need Depression and Anxiety or type "exit": ')).lower()
        self.chronic_pain = str(input(f'Input "3 and Enter" if need Chronic Pain or type "exit": ')).lower()
        self.reduced_addictive_cravings = str(
            input(f'Input "4 and Enter" if need Reduced Addictive Cravings or type "exit": ')).lower()
        self.imp_motor_skills_learning = str(
            input(f'Input "5 and Enter" if need Improved Motor Skills and Learning or type "exit": ')).lower()
        self.improved_insight = str(input(f'Input "6 and Enter" if need Improved Improved Insight or type "exit": ')).lower()
        self.reduced_risk_taking = str(input(f'Input "7 and Enter" if need Reduced Risk Taking or type "exit": ')).lower()
        self.increased_present_awareness = str(
            input(f'Input "8 and Enter" if need Increased Present Awareness or type "exit": ')).lower()
        self.math = str(input(f'Input "9 and Enter" need Improved Mathematical Abilities or type "exit":')).lower()
        self.pitch_perception = str(input(f'Input "10 and Enter" need Pitch Perception or type "exit":')).lower()
        self.improved_attention = str(input(f'Input "11 and Enter" need Improved Attention:')).lower()
        self.memory_learning = str(input(f'Input "12 and Enter" if need Memorization and Learning or type "exit": ')).lower()
        self.alternate_depression_treatment = str(
            input(f'Input "13 and Enter" if need Alternate Depression Treatment or type "exit": ')).lower()
        self.improved_socialization = str(input(f'Input "14 and Enter" if need Improved Socialization or type "exit": ')).lower()

    def accel_learn(self):
        if '1' in self.accelerated_learning:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/accelerated-learning-darpa-montage/')
        else:
            print('\n1. You did not choose Accelerated Learning')

    def depress_and_anxiety(self):
        if '2' in self.depression_and_anxiety:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/depression-and-anxiety/')
        else:
            print('\n2. You did not choose Depression and Anxiety')

    def chron_pain(self):
        if '3' in self.chronic_pain:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/chronic-pain/')
        else:
            print('\n3. You did not choose Chronic Pain')

    def reduc_addictive_cravings(self):
        if '4' in self.reduced_addictive_cravings:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/cravings-and-addictions/')
        else:
            print('\n4. You did not choose Reduced Addictive Cravings')

    def imp_mot_sk_learning(self):
        if '5' in self.imp_motor_skills_learning:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/improved-motor-skills-learning/')
        else:
            print('\n5. You did not choose Improved Motor Skills and Learning')

    def impr_insight(self):
        if '6' in self.improved_insight:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/improved-insight/')
        else:
            print('\n6. You did not choose Improved Insight')

    def reduc_risk_taking(self):
        if '7' in self.reduced_risk_taking:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/reduced-risk-taking/')
        else:
            print('\n7. You did not choose Reduced Risk Taking')

    def incr_present_awareness(self):
        if '8' in self.increased_present_awareness:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/increased-present-awareness/')
        else:
            print('\n8. You did not choose Increased Present Awareness')

    def mathem(self):
        if '9' in self.math:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/improved-mathematical-abilities/')
        else:
            print('\n9. You did not choose Improved Mathematical Abilities')

    def pitch_percep(self):
        if '10' in self.pitch_perception:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/pitch-perception/')
        else:
            print('\n10. You did not choose Pitch Perception')

    def impr_attention(self):
        if '11' in self.improved_attention:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/improved-attention/')
        else:
            print('\n11. You did not choose Improved Attention')

    def mem_learning(self):
        if '12' in self.memory_learning:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/memorization-and-learning/')
        else:
            print('\n12. You did not choose Memorization and Learning')

    def alter_depression_treatment(self):
        if '13' in self.alternate_depression_treatment:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/alternative-depression-treatment/')
        else:
            print('\n13. You did not choose Alternate Depression Treatment')

    def impr_socialization(self):
        if '14' in self.improved_socialization:
            driver = webdriver.Chrome()
            driver.get('https://totaltdcs.com/electrode-placement-montage-list/improved-socialization/')
        else:
            print('\n14. You did not choose Improved Socialization')


tdcs_1 = tdcs_choose_feature('', '', '', '', '', '', '', '', '', '', '', '', '', '')
tdcs_1.accel_learn()  # 1
tdcs_1.depress_and_anxiety()  # 2
tdcs_1.chron_pain()  # 3
tdcs_1.reduc_addictive_cravings()  # 4
tdcs_1.imp_mot_sk_learning()  # 5
tdcs_1.impr_insight()  # 6
tdcs_1.reduc_risk_taking()  # 7
tdcs_1.incr_present_awareness()  # 8
tdcs_1.mathem()  # 9
tdcs_1.pitch_percep()  # 10
tdcs_1.impr_attention()  # 11
tdcs_1.mem_learning()  # 12
tdcs_1.alter_depression_treatment()  # 13
tdcs_1.impr_socialization()  # 14
