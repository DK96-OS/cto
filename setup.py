"""Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="commit-text-organizer",
    version="1.0.1",
    description="A Text Processor Targeted at Organizing Commit Messages.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="DK96-OS",
    url="https://github.com/DK96-OS/cto",
    project_urls={
        "Issues": "https://github.com/DK96-OS/cto/issues",
        "Source Code": "https://github.com/DK96-OS/cto"
    },
    license="GPLv3",
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'commit-text-organizer=commit_text_organizer.__main__:main',
            'commit_text_organizer=commit_text_organizer.__main__:main',
            'cto=commit_text_organizer.__main__:main',
        ],
    },
    python_requires='>=3.10',
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
