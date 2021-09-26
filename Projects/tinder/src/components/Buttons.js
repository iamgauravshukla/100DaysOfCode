import React from 'react'
import '../buttons.css'
// Icons
import ReplayIcon from '@mui/icons-material/Replay';
import CloseIcon from '@mui/icons-material/Close';
import StarRateIcon from '@mui/icons-material/StarRate';
import FavoriteIcon from '@mui/icons-material/Favorite';
import FlashOnIcon from '@mui/icons-material/FlashOn';
import { IconButton } from '@mui/material';

function Buttons() {
    return (
        <div className='buttons-container'>
            <IconButton className="btn-repeat">
                <ReplayIcon fontSize="large" />
            </IconButton>
            <IconButton className="btn-left">
                <CloseIcon fontSize="large" />
            </IconButton>
            <IconButton className="btn-star">
                <StarRateIcon fontSize="large" />
            </IconButton>
            <IconButton className="btn-right">
                <FavoriteIcon fontSize="large" />
            </IconButton>
            <IconButton className="btn-lighting">
                <FlashOnIcon fontSize='large' />
            </IconButton>
        </div>
    )
}

export default Buttons
