# import torch
# print(torch.__version__)
# print(torch.cuda.is_available())

import numpy as np

def test(*args):
    print(*args)

def random_rotation_translation(t):
    m = np.random.normal(size=[3, 3])
    m[1] = np.cross(m[0], m[2])
    m[2] = np.cross(m[0], m[1])
    m = m / np.linalg.norm(m, axis=1, keepdims=True)
    m = np.pad(m, [[0, 1], [0, 1]], mode='constant')
    m[3, 3] = 1.0
    m[:3, 3] = np.random.uniform(-t, t, size=[3])
    return m

if __name__ == '__main__':
    r_rot = random_rotation_translation(0.25)
    print(r_rot)
    r_rot[0] = 0
    print(r_rot)
    r_rot[0, 0] = 1
    print(r_rot)
    r_rot[:2, 0] = 2
    print(r_rot)