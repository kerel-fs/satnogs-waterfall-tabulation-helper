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
```
./rffit -d $SATNOGS_OBS_DIR/1102230.dat -i 44356 -c $SATNOGS_TLE_DIR/1102230.txt -s 7669
```

## Other commands

- Download the TLE used for a specific SatNOGS Observation:
  ```
  ./contrib/download_satnogs_tle.py $OBSERVATION_ID
  ```

## Known issues

- Only SatNOGS stations <999 are supported! The strf sites.txt parser supports 4-digit site ids only.
  In case of problems, modity the `site_id` in the doppler obs (`.dat`-files, last column) to something valid,
  and modify the respective entry in `sites.txt`. By default the tabulation-helper will generate a `site_id` of
  the form `7{station_id}`, e.g. station 669 will result in `site_id=7669`.

## Advanced configuration

For backward compatibility all data paths can be customized. The following configuration fields are available:
- `SATNOGS_TLE_DIR`
- `SATNOGS_WATERFALL_IMAGES_DIR`
- `SATNOGS_ARTIFACTS_DIR`
- `SATNOGS_DOPPLER_OBS_DIR`
- `SATNOGS_OBSERVATIONS_DIR`
- `SATNOGS_SITES_TXT`
