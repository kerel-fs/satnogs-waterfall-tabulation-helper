#!/usr/bin/env python3

import argparse
import os

from settings import strf_path
from satnogs_api_client import fetch_observation_data


def download_satnogs_tle(observation_id):
    filename = strf_path.observation_tle(observation_id)

    if os.path.exists(filename):
        # Skip
        print(f'TLE for {observation_id} exists already, skip.')
        return

    obs = fetch_observation_data([observation_id])[0]

    with open(filename, 'w') as f:
        f.write(obs['tle0'])
        f.write('\n')
        f.write(obs['tle1'])
        f.write('\n')
        f.write(obs['tle2'])
        f.write('\n')
    print("TLE saved in {}".format(filename))


if __name__ == '__main__':
    strf_path.init_paths()

    parser = argparse.ArgumentParser(description='Download TLE from a specific Observation in SatNOGS Network.')
    parser.add_argument('observation_id', type=int,
                        help='SatNOGS Observation ID')
    args = parser.parse_args()

    download_satnogs_tle(args.observation_id)
