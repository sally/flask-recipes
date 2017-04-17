# Local setup

Make sure you are running Python 2.7.3. You can check the version of Python you are using by doing:

```
python -V
```

Install the required packages by running:

```
pip install requirements.txt
```

Boot the server by running:

```
python run.py
```

For some reason, doing `flask run` doesn't work. We get "ImportError: Import by filename is not supported." errors.

# Helpful References

[Patrick's Software Blog - Flask Tutorial](http://www.patricksoftwareblog.com/flask-tutorial/)

[Explore Flask - Functional vs Divisional Structure for Blueprints](http://exploreflask.readthedocs.io/en/latest/blueprints.html#where-do-you-put-them)
