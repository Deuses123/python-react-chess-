import React from 'react';
import { ReactComponent as BP } from './bP.svg';
import { ReactComponent as BB } from './bB.svg';
import { ReactComponent as BK } from './bK.svg';
import { ReactComponent as BN } from './bN.svg';
import { ReactComponent as BQ } from './bQ.svg';
import { ReactComponent as BR } from './bR.svg';

import { ReactComponent as WP } from './wP.svg';
import { ReactComponent as WB } from './wB.svg';
import { ReactComponent as WK } from './wK.svg';
import { ReactComponent as WN } from './wN.svg';
import { ReactComponent as WQ } from './wQ.svg';
import { ReactComponent as WR } from './wR.svg';

const Pieces = ({ type }) => {
    switch (type) {
        case 'bP':
            return <BP />;
        case 'bB':
            return <BB />;
        case 'bK':
            return <BK />;
        case 'bN':
            return <BN />;
        case 'bQ':
            return <BQ />;
        case 'bR':
            return <BR />;

        case 'wP':
            return <WP />;
        case 'wB':
            return <WB />;
        case 'wK':
            return <WK />;
        case 'wN':
            return <WN />;
        case 'wQ':
            return <WQ />;
        case 'wR':
            return <WR />;

        default:
            return '♔';
    }
};

export default Pieces;
