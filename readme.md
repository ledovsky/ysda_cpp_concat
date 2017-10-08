# CPP Concat

Script for concatenating your CPP project into one file for YSDA algorithms
course homeworks or Yandex.Contest or for anything where it suits

Usage. Copy cpp_concat.py to your project root and run it. For example:

    python cpp_concat.py config.json

It's expected you have Python 3 and your files are in UTF-8

In simple JSON config you should provide files (all paths are relative) in order they should be joined and also the output file.

```json
{
    "files": [
        "file.h",
        "file.cpp",
        "main.cpp"
    ],
    "out_fn": "main_out.cpp"
}
```

Pull requests are welcome.

Author: Alexander Ledovsky, 2017
