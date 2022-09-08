#!/usr/bin/python3

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

extensions = {
    "csvmagic.processor": {
        "sources": [
            "csvmagic/processor/module.c",
            "csvmagic/processor/CSVProcessor/definition.c",
            "csvmagic/processor/CSVProcessorMode/definer.cpp",
            "csvmagic/processor/generic_utils/enum.cpp",
        ],
        "extra_compile_args": {
            "msvc": [
                "/WX",
            ],
            "unix": [
                "-Werror",
            ],
        },
    }
}


class ExtraCompileArgsExtension(build_ext):
    def build_extension(self, ext: Extension):
        extra_args = extensions[ext.name].get("extra_compile_args")
        if extra_args is not None:
            ctype = self.compiler.compiler_type
            ext.extra_compile_args = extra_args[ctype]

        build_ext.build_extension(self, ext)


setup(
    name="csvmagic",
    version="0.0.1",
    license="GNU GPLv3",

    description="CSV processing library",
    author="Florian Schieder",
    author_email="florian.schieder@web.de",

    packages=[
        "csvmagic",
    ],
    ext_modules=[
        Extension(it[0], **it[1])
        for it in extensions.items()
    ],
    cmdclass={'build_ext': ExtraCompileArgsExtension},
)
