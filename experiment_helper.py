from psychopy import locale_setup, sound, gui, visual, core, data
from collections import OrderedDict
import random


def exp_info_GUI(name, default_info):
    info = default_info
    dlg = gui.DlgFromDict(dictionary=default_info, title=name)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    info['date'] = data.getDateStr()  # add a simple timestamp
    info['exp_name'] = name
    return info


def exp_handler_setup(name, info, filename):
    return  data.ExperimentHandler( name=name, version='',
                                    extraInfo=info, runtimeInfo=None,
                                    originPath=None,
                                    savePickle=True, saveWideText=True,
                                    dataFileName=filename)


def create_window(size, fullscr, screen, units):
    win = visual.Window(
        size=size, fullscr=fullscr, screen=screen,
        allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units=units)
    return win


# def main_trial_list(diff_trial_list_1, same_trial_list_1, diff_trial_list_2, same_trial_list_2,
#                     diff_trial_list_3, same_trial_list_3):
#     trial_dict = OrderedDict([
#                             ("exp1", [diff_trial_list_1, same_trial_list_1]),
#                             ("exp2", [diff_trial_list_2, same_trial_list_2]),
#                             ("exp3", [diff_trial_list_3, same_trial_list_3])
#                             ])
#     items = trial_dict.items()
#     random.shuffle(items)
#     trial_dict = OrderedDict(items)
#     for key, value in trial_dict.items():
#         random.shuffle(value)
#     combined_trial_list = list()
#     for key, value in trial_dict.items():
#         for val in value:
#             for trials in val:
#                 combined_trial_list.append(trials)
#     return combined_trial_list


# def exp_1(same_list, diff_list, target_present, same_cond, load):
#     letters = []
#     for i in range(load):
#         if target_present == 'yes' and same_cond == 'same':
#             if i < load - 1:
#                 letters.append(diff_list[i])
#             else:
#                 letters.append(same_list[i])
#         elif target_present == 'no' and same_cond == 'same':
#             letters.append(diff_list[i])
#         elif target_present == 'yes' and same_cond == 'different':
#             if i < load - 1:
#                 letters.append(same_list[i])
#             else:
#                 letters.append(diff_list[i])
#         elif target_present == 'no' and same_cond == 'different':
#             letters.append(same_list[i])
#     return letters


# def exp_2(same_list, diff_list, target_present, same_cond, load):
#     letters = []
#     if target_present == 'yes' and same_cond == 'same':
#         for j in range(load - 1):
#             letters.append(diff_list[j])
#         letters.append(same_list[j])
#     elif target_present == 'no' and same_cond == 'same':
#         for j in range(load):
#             letters.append(diff_list[j])
#     elif target_present == 'yes' and same_cond == 'different':
#         for j in range(load - 1):
#             letters.append(same_list[j])
#         letters.append(diff_list[j])
#     elif target_present == 'no' and same_cond == 'different':
#         for j in range(load):
#             letters.append(same_list[j])
#     return letters


# def exp_3(target_present, letter, pair, load):
#     letters = []
#     if target_present == 'yes':
#         for i in range(load - 1):
#             letters.append(pair)
#         letters.append(letter)
#     elif target_present == 'no':
#         for i in range(load):
#             letters.append(pair)
#     random.shuffle(letters)
#     return letters

