from setuptools import setup

description = "Simplified ARIA2c based url downloader, makes it easy to download a large number of urls"

setup(
    name="parallel_url_downloader",
    version="0.1.0",
    author="Mehdi Cherti, Sam Sepiol",
    description=description,
    license="MIT",
    url="https://github.com/mehdidc/parallel_url_downloader",
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['parallel_url_downloader'],
    include_package_data=True,
    install_requires=['clize', 'joblib'],
)
