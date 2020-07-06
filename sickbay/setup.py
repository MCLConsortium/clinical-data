# encoding: utf-8

import setuptools, os.path


_requirements = [
    'setuptools',
    'psycopg2',
    'sqlalchemy'
]


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), 'r') as f: desc = f.read()


setuptools.setup(
    name='mcl.sickbay',
    version='0.0.0',
    description='Clinical Data',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Sean Kelly',
    author_email='sean.kelly@jpl.nasa.gov',
    url='https://github.com/MCLConsortium/clinical-data',
    namespace_packages=['mcl'],
    test_suite='mcl.sickbay.tests.test_suite',
    packages=setuptools.find_packages({'': 'src'}),
    package_data={
        '': ['*.txt', '*.md', '*.rst']
    },
    include_package_data=True,
    zip_safe=True,
    install_requires=_requirements,
    license='ALv2',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
