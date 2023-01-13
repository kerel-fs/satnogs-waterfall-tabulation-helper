# Installation & Usage Guide

## Installation

```{note}
It is recommended to [create a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
and to run all commands inside inside it.
```

Dependencies get installed with:
```
pip install -r requirements.txt
```

# Configuration

Copy the file `env-dist` to `.env` and add your SatNOGS DB API Token. This can be found at [SatNOGS DB: User page](https://db.satnogs.org/users/edit) (you must be logged-id).
All data files produced by this application are managed at `~/.local/share/satnogs-tabulation-helper/`.

## Usage

To analyze the waterfall image from SatNOGS Observation ID 1102230, run

```bash
./satnogs_waterfall_tabulation_helper.py 1102230
```

An interactive plot will show up.
Clicking inside the plot will add a signal marker.
If you are finished with adding signal markers,
save the signal markers using the keyboard shortcut `f`.

Custom keyboard shortcuts:
```text
u - undo last signal marker
f - save the signal markers in an strf-compatible file
```

Useful Matplotlib navigation keyboard shortcuts:
```text
p - toggle 'Pan/Zoom' modus
o - toggle 'Zoom-to-rect' modus
h - Home/Reset (view)
c - Back (view)
```

If you have strf rffit installed, use it to for orbit fitting:
Since path handling with STRF is complicated sometimes, the tabulation helper can output a hint text on
using rffit when called with the argument `--show-hint`:

```
❯ ./satnogs_waterfall_tabulation_helper.py 806927 --show-hint
WARNING: NORAD ID mismatch between Observation Metadata and TLE (44420 vs 44339)!
Use NORAD ID from TLE for rffit.
[...]
INFO: Stored 4 selected track points in /home/kerel/.local/share/satnogs-tabulation-helper/doppler_obs/806927.dat

Modify the following line:
ST_DATADIR="$HOME/src/strf" # path to your strf directory

Then run the following commands:
cd $ST_DATADIR

STH_DATA_DIR="/home/kerel/.local/share/satnogs-tabulation-helper"
OBS_ID=806927
SITE_ID=50
NORAD_ID=44339

ST_TLEDIR=$STL_DATA_DIR/tles
ST_COSPAR=50

export ST_DATADIR
export ST_TLEDIR
export ST_COSPAR

./rffit -d $STH_DATA_DIR/doppler_obs/$OBS_ID.dat -i $NORAD_ID -c $STH_DATA_DIR/tles/$OBS_ID.txt -s $SITE_ID
```

## Other commands

- Download the TLE used for a specific SatNOGS Observation:
  ```
  ./contrib/download_satnogs_tle.py $OBSERVATION_ID
  ```

## Known limitations

- The `site_id` in data files is set to the SatNOGS Station ID. When using STRF, make sure to either
  use a `sites.txt` with COSPAR IDs or with SatNOGS Station IDs. A previous version of the SatNOGS
  Waterfall Tabulation Helper performed a mapping of SatNOGS Station IDs,
  e.g. station 669 became `site_id` 7669. Thus only SatNOGS stations <999 were supported.

## Advanced configuration

For backward compatibility all data paths can be customized. The following configuration fields are available:
- `SATNOGS_TLE_DIR`
- `SATNOGS_WATERFALL_IMAGES_DIR`
- `SATNOGS_ARTIFACTS_DIR`
- `SATNOGS_DOPPLER_OBS_DIR`
- `SATNOGS_OBSERVATIONS_DIR`
- `SATNOGS_SITES_TXT`
