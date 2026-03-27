import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'turtle_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Required: registers the package with ament's resource index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # Required: installs package.xml so ros2 pkg can find this package
        ('share/' + package_name, ['package.xml']),
        # Required: installs all .py launch files into the package's share directory
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@ksu.edu',
    description='Turtlesim bringup launch package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # No executable nodes in this package — launch files only
        ],
    },
)
