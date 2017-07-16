from setuptools import setup

setup_kwargs = {
    'name': 'splot',
    'version': '0.0.1',
    'description': 'BG standard figure Tools',
    'url': 'http://gitlab.thebillingegroup.com/analysis/17sx_plotting',
    'classifiers': [
        'License :: LISENSE',
        'Target Audience :: BG students',
        'Programming Language :: Python :: 3',
        ],
    'zip_safe': False,
    'packages': ['splot'],
    'package_dir': {
        'splot': 'splot',
        },
    'data_files': [('splot/styles', ['*.mplstyle'])],
    }
    
if __name__ == '__main__':
    setup(**setup_kwargs)