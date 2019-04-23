import sys
try:
    # Setuptools entry point is slow.
    # If we have `festentrypoint` then use a fast entry point
    import fastentrypoints
except ImportError:
    sys.stdout.write('Not using fastentrypoints\n')
    pass


import setuptools
import os

HERE = os.path.dirname(__file__)

setuptools.setup(
    name='i3-workspace-switcher',
    version="0.1.0",
    author='un-def',
    author_email='me@undef.im',
    description='i3 MRU workspace switcher',
    license='MIT',
    keywords='',
    url='',
    long_description='',
    entry_points={
        'console_scripts': ['i3-workspace-switcher=i3_workspace_switcher:main']
    },
    install_requires=['i3ipc']
)
