# Changelog
## Unreleased
- Fixed data path (correct path: `~/.local/share/satnogs-tabulation-helper/`)
- Fixed marker input (rounded to nearest integer pixel value).
- Added STRF rffit hint text (by using `--show-hint`).

## 0.2

First release,
code imported from [kerel-fs/strf@2efec5](https://gitlab.com/kerel-fs/strf/-/commit/2efec5a386dfe2888cc85dc3628a7812d33f4ffc).

- No preparation of data directories needed anymore. This will be done automatically.
  Data is stored in `~/.local/share/satnogs-tabulation-helper/` now.
