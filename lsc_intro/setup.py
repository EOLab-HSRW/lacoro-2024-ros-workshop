from setuptools import find_packages, setup

package_name = 'lsc_intro'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lacoro',
    maintainer_email='harley.lara@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f"image = {package_name}.image:main",
            f"simple_proc = {package_name}.simple_proc:main",
            f"detection = {package_name}.detection:main"
        ],
    },
)
