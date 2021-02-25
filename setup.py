from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


setup(
    name='curve_evaluation',
    ext_modules=[
        CUDAExtension(name='curve_eval_cuda',
            sources=['curve_evaluation/csrc/curve_eval_cuda.cpp',
            'curve_evaluation/csrc/curve_eval_cuda_kernel.cu']),
        # CppExtension(name='curve_eval_cpp',
        # sources=['curve_evaluation/csrc/curve_eval.cpp'],
        # extra_include_paths=['curve_evaluation/csrc/curve_eval.h'])
    ],
    cmdclass={
        'build_ext': BuildExtension
    },
    packages=find_packages()
    
    )
