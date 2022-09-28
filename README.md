# Data for Nipraxis course

See: <https://nipraxis.org>

## Adding / removing / updating data files

Calculate the MD5 hash for the file, e.g.

```
md5 ds108_sub001_t1r1.nii
```

This will give you something like:

```
ds108_sub001_t1r1.nii) = 6378302aad7bc006bfb48fa973866e68
```

Registry is at <https://github.com/nipraxis/nipraxis> in the
`nipraxis/_fetcher.py` file.  Update hashes for changed files there, add a line
like:

```
    'ds108_sub001_t1r1.nii': 'md5:6378302aad7bc006bfb48fa973866e68',
```

Don't forget to tag new releases here in the `nipraxis-data` repo, as in:

```
git tag -s 0.4
git push
git push --tags
```

The change the corresponding data version in the Nipraxis package, as in (`_fetcher.py`):

```python
DATA_VERSION = '0.4'
```

Then (for Nipraxis) update version in `__init__.py` push, and tag and release
to PyPI.
