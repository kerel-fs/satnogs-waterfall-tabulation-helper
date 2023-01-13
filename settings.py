import sys
import os

from pathlib import Path
from decouple import config, UndefinedValueError

home_dir = os.path.expanduser('~')
xdg_data_dir = Path(home_dir, '.local/share/satnogs_tabulation_helper/')

try:
    TLE_DIR = config('SATNOGS_TLE_DIR', default=Path(xdg_data_dir, 'tles'))
    WATERFALL_IMAGES_DIR = config('SATNOGS_WATERFALL_IMAGES_DIR', default=Path(xdg_data_dir, 'waterfalls'))
    ARTIFACTS_DIR = config('SATNOGS_ARTIFACTS_DIR', default=Path(xdg_data_dir, 'artifacts'))
    DOPPLER_OBS_DIR = config('SATNOGS_DOPPLER_OBS_DIR', default=Path(xdg_data_dir, 'doppler_obs'))
    OBSERVATIONS_DIR = config('SATNOGS_OBSERVATIONS_DIR', default=Path(xdg_data_dir, 'observations'))
    SITES_TXT = config('SATNOGS_SITES_TXT', default=Path(xdg_data_dir, 'sites.txt'))


    SATNOGS_NETWORK_API_URL = config('SATNOGS_NETWORK_API_URL', default="https://network.satnogs.org/api/")
    SATNOGS_DB_API_URL = config('SATNOGS_DB_API_URL', default="https://db.satnogs.org/api/")
    SATNOGS_DB_API_TOKEN = config('SATNOGS_DB_API_TOKEN')
except UndefinedValueError as err:
    print("Missing Environment Variable.")
    print(err)
    sys.exit(-1)

class strf_path:
    def init_paths():
        # Make sure xdg-data-dir for this application exists
        xdg_data_dir.mkdir(exist_ok=True)
        for subdir in ['tles', 'waterfalls', 'artifacts', 'doppler_obs', 'observations']:
            Path(xdg_data_dir, subdir).mkdir(exist_ok=True)
        if not Path(xdg_data_dir, 'sites.txt').exists():
            Path(xdg_data_dir, 'sites.txt').touch()

    def artifact(observation_id):
        return '{}/{}.h5'.format(ARTIFACTS_DIR, observation_id)
    def doppler_obs(observation_id):
        return '{}/{}.dat'.format(DOPPLER_OBS_DIR, observation_id)
    def observation_tle(observation_id):
        return '{}/{}.txt'.format(TLE_DIR, observation_id)
    def observation(observation_id):
        return '{}/{}.json'.format(OBSERVATIONS_DIR, observation_id)
    def sites_txt():
        return SITES_TXT
    def waterfall_image(observation_id):
        return '{}/{}.png'.format(WATERFALL_IMAGES_DIR, observation_id)
