from setuptools import setup


setup(
    name="igi_lab3",
    version="1.0",
    description="library for python serialization",
    url="",
    author="Egor Chyzhou",
    author_email="egor.chijov@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers/json_serializer", "serializers/src",
              "serializers/xml_serializer", "serializers"],
    include_package_data=True
)