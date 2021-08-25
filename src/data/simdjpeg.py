import os
from data import srdata
from data import simd

class SIMDJPEG(simd.SIMD):
    def __init__(self, args, name='', train=True, benchmark=False):
        self.q_factor = int(name.replace('SIMD-Q', ''))
        super(SIMDJPEG, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )

    def _set_filesystem(self, dir_data):
        self.apath = os.path.join(dir_data, 'SIMD')
        self.dir_hr = os.path.join(self.apath, 'SIMD_train_HR')
        self.dir_lr = os.path.join(
            self.apath, 'SIMD_Q{}'.format(self.q_factor)
        )
        if self.input_large: self.dir_lr += 'L'
        self.ext = ('.png', '.jpg')

