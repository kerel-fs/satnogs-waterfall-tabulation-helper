# SatNOGS Waterfall Tabulation Helper

Repository: [kerel-fs/satnogs-waterfall-tabulation-helper](https://gitlab.com/kerel-fs/satnogs-waterfall-tabulation-helper)

The SatNOGS Waterfall Tabulation helper is a script to extract rough doppler measurements
from SatNOGS waterfall png files. It downloads the waterfall png and obervation metadata and
allows the user to extract doppler measurements interactively.
Those measurements are stored in a STRF-compatible data file.

## Installation & Usage

Follow the  [Usage Guide](./docs/usage_guide.md).

## History

This tool evolved from the need to tabulate doppler data from waterfall images by DF2MZ of the lunar Change-4 probe,
see [DF2MZ Doppler Measurements](https://gitlab.com/kerel-fs/jupyter-notebooks/tree/master/change4/data#df2mz-doppler-measurements).
It was adjusted to read SatNOGS waterfall pngs instead and extended to
remove the doppler correction performed by the satnogs-client during the observation.
Its purpose is similar to rfplot in [STRF](https://github.com/cbassa/strf).

Original release post: [New software: SatNOGS waterfall tabulation helper](https://community.libre.space/t/new-software-satnogs-waterfall-tabulation-helper/4380)

From 2021-11-20 until 2023-01-13 it was maintained as part of [STRF](https://github.com/cbassa/strf).

While still supporting strf, 2023-01-13 it was moved into its own repository at
[kerel-fs/satnogs-waterfall-tabulation-helper](https://gitlab.com/kerel-fs/satnogs-waterfall-tabulation-helper)
to ease the development process.

## License

AGPL-3.0-or-later
