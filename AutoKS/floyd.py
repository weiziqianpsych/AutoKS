#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def floyd(dis, r=np.inf):
    """

    Roger Schvaneveldt (2021).
    Pathfinder Networks
    (https://www.mathworks.com/matlabcentral/fileexchange/59378-pathfinder-networks),
    MATLAB Central File Exchange. Retrieved March 23, 2021.



    Copyright (c) 2016, Roger Schvaneveldt
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
      list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    mindis = floyd(dis,r)
    dis    | dissimilarity matrix
    r      | value of the r parameter
    mindis | minimum distance between nodes
    links  | links in the PFnet(q=n-1,r)
    (based on Floyd algorithm for finding shortest paths)

    in this function, parameter q = n - 1, n = number of nodes

    """

    mindis = dis.copy()

    for ind in range(0, dis.shape[0]):
        for row in range(0, dis.shape[0]):
            for col in range(0, dis.shape[0]):
                # indirect = minkowski(mindis(row,ind), mindis(ind,col),r)
                indirect = np.linalg.norm([mindis[row, ind], mindis[ind, col]], r)
                if indirect < mindis[row, col]:
                    mindis[row, col] = indirect

    tflinks = (dis < np.inf) & (abs(mindis - dis) < 1e-14)

    return tflinks
