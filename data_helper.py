from psychopy import data


def create_trial_database(n_trials, exp_info, name, method = 'fullRandom'):
    return data.TrialHandler(nReps=n_trials, method='fullRandom',
        extraInfo=exp_info, originPath=-1,
        trialList=[None],
        seed=None, name=name)


def save_loc_data(trials, letters, pos):
    for ind, (x, y) in enumerate(pos):
        trials.addData("stim{}.letters".format(ind), letters[ind])
        trials.addData("stim{}.x".format(ind), x)
        trials.addData("stim{}.y".format(ind), y)
    return trials


def save_cond(trials, load, cond, target_present):
    trials.addData("load", load)
    trials.addData("target_present", target_present)
    trials.addData("cond", cond)
    return trials


def save_response(trials, response, rt, correct_ans):
    trials.addData('response', response)
    trials.addData('rt', rt)
    trials.addData('correct_ans', correct_ans)
    return trials


def save_trial_file(trials, filename):
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsText(filename + '_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])


def save_exp_file(thisExp, filename):
    thisExp.saveAsWideText(filename+'.csv')
    thisExp.saveAsPickle(filename)
