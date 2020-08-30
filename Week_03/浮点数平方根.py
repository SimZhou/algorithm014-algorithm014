def sqrtNewton(m):
    # 牛顿法
    # x的平方根：sq = sqrt(m), sq**2 = m
    # 求sq，即为求 y = sq**2 - m 的根（when y=0）
    # sq == sq0 位置的切线为：y-y0 = 2*sq0*(sq-sq0)  其中 y0 = sq0**2 - m
    # 于是，切线的根位置为y=0时的sq值：m-sq0**2 = 2*sq0*sq - 2*sq0**2
    # 整理后可得：sq = (m + sq0**2)/(2*sq0)
    # 函数图像在此；http://suo.nz/5pl3Te
    # 所以，只要迭代此公式，直到收敛即可
    sq = m
    while 1:
        new_sq = (m + sq**2)/(2*sq)
        if abs(new_sq - sq) < 1e-15: break
        sq = new_sq
    return sq