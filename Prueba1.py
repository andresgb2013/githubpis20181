# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:28:00 2018

@author: Usuario
"""

import os.path as op
import mne
from mne.datasets.sample import data_path

fname = op.join(data_path(), 'MEG', 'sample', 'sample_audvis_raw.fif')
raw = mne.io.read_raw_fif(fname).crop(0, 10)
original_level = mne.get_config('MNE_LOGGING_LEVEL', 'INFO')