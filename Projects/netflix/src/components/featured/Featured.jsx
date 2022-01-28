import React from 'react'
import './featured.scss'
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';

export default function Featured({type}) {
    return (
        <div className="featured">
            {type && (
                <div className="category">
                    <span>{type === "movie" ? 'Movies' : 'Series'}</span>
                    <select name="genere" id="genre">
                        <option>Genre</option>
                        <option value="adventure">Adventure</option>
                        <option value="comedy">Comedy</option>
                        <option value="crime">Crime</option>
                        <option value="fantasy">Fantasy</option>
                        <option value="historical">Historical</option>
                        <option value="horror">Horror</option>
                        <option value="romance">Romance</option>
                        <option value="sci-fi">Sci-fi</option>
                        <option value="thriller">Thriller</option>
                        <option value="western">Western</option>
                        <option value="animation">Animation</option>
                        <option value="drama">Drama</option>
                        <option value="documentary">Documentary</option>
                    </select> 
                </div>
            )}
            <img src="https://images3.alphacoders.com/107/1072835.jpg" alt="" />
            
            <div className="info">
                <img src="https://occ-0-2433-999.1.nflxso.net/dnm/api/v6/tx1O544a9T7n8Z_G12qaboulQQE/AAAABYU8-zdFN3IFeLKeO7_q0dIsDD_KlWExxpKi-sVTbwj75KYPPWj7MU-gdP8oiEV_i0w7RRSu5nKpY5-lf7BEfZDuqK0hgv0fjGHXUPnCantrxE07GbripYBZQLEW1t4osyRUEqiODu3km3wySnllK9GIrRNH0bFnvBwatmXRN8Lk2A.png?r=a59" alt="" />
                <span className="desc">
                A hardened mercenary's mission becomes a soul-searching race to survive when he's 
                sent into Bangladesh to rescue a drug lord's kidnapped son.
                </span>
                <div className="buttons">
                    <button className="play">
                        <PlayArrowIcon/>
                        <span>Play</span>
                    </button>
                    <button className="more">
                        <InfoOutlinedIcon/>
                        <span>Info</span>
                    </button>
                </div>
            </div>
        </div>
    )
}
