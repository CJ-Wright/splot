from setuptools import setup

setup_kwargs = {
    'name': 'splot',
    'version': 'v0.1',
    'description': 'BG standard figure Tools',
    'url': 'http://gitlab.thebillingegroup.com/analysis/17sx_plotting',
    'classifiers': [
        'License :: LISENSE',
        'Target Audience :: BG students',
        'Programming Language :: Python :: 3',
        ],
    'zip_safe': False,
    'packages': ['splot', 'examples'],
    'package_dir': {
        'splot': 'splot',
        'examples': 'examples',
        },
    'data_files': [('examples/data', ['*.'])],
    }
    
if __name__ == '__main__':
    setup(**setup_kwargs)