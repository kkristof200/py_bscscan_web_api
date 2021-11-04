import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'bscscan_web_api'

setuptools.setup(
    name='bscscan_web_api',
    version='0.0.4',
    author='Kristóf-Attila Kovács',
    description='bscscan_web_api',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/py_bscscan_web_api',
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4>=4.10.0',
        'jsoncodable>=0.1.7',
        'ksimpleapi>=0.0.40',
        'noraise>=0.0.16',
        'requests>=2.26.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)