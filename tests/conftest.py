"""Configure tests."""
import mne
import pytest
from mne.datasets import eegbci


@pytest.fixture(scope="session")
def montage():
    """Fixture for standard EEG montage."""
    montage_kind = "standard_1020"
    return mne.channels.make_standard_montage(montage_kind)


@pytest.fixture(scope="session")
def raw():
    """Fixture for physionet EEG subject 4, dataset 1."""
    mne.set_log_level("WARNING")
    # load in subject 1, run 1 dataset
    edf_fpath = eegbci.load_data(4, 1, update_path=True)[0]

    # using sample EEG data (https://physionet.org/content/eegmmidb/1.0.0/)
    raw = mne.io.read_raw_edf(edf_fpath, preload=True)

    # The eegbci data has non-standard channel names. We need to rename them:
    eegbci.standardize(raw)

    return raw
