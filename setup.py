from setuptools import setup
from yuyu import __version__

setup(
    name="yuyu",
    version=__version__,
    author="yuyuteam",
    author_email="support@yuyu-billing.dev",
    url="http://yuyu-billing.dev",
    description="yuyu billing",
    long_description="yuyu billing",
    license="...",
    scripts=[
        "bin/process_invoice.sh",
        "bin/setup_api.sh",
        "bin/setup_event_monitor.sh",
    ],
    packages=[
        "yuyu",
        "yuyu.api",
        "yuyu.core",
        "yuyu.core.component",
        "yuyu.core.management",
        "yuyu.core.management.commands",
        "yuyu.core.migrations",
        "yuyu.core.utils",
    ]
)
