import React, { useState } from 'react'
import './listitem.scss'
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import ThumbUpAltOutlinedIcon from '@mui/icons-material/ThumbUpAltOutlined';
import ThumbDownAltOutlinedIcon from '@mui/icons-material/ThumbDownAltOutlined';
import AddIcon from '@mui/icons-material/Add';
export default function ListItem({ index }) {

    const [isHovered, setIsHovered] = useState(false);
    const trailer = "https://player.vimeo.com/external/371433846.sd.mp4?s=236da2f3c0fd273d2c6d9a064f3ae35579b2bbdf&profile_id=139&oauth2_token_id=57447761"
    return (
        <div className="listitem"
            style={{ left: isHovered && index * 225 - 50 + index * 2.5 }}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}>
            <img src="https://i.ytimg.com/vi/v4hS2AiqUYU/maxresdefault.jpg" alt="" />
            {isHovered && (
                <>
                    <video src={trailer} autoPlay={true} loop></video>
                    <div className="itemInfo">
                        <div className="icons">
                            <PlayArrowIcon className= "icon"/>
                            <AddIcon className= "icon"/>
                            <ThumbUpAltOutlinedIcon className= "icon"/>
                            <ThumbDownAltOutlinedIcon className= "icon"/>
                        </div>
                        <div className="infoTop">
                            <span>2hr 10 mins</span>
                            <span className="ageLimit">+14</span>
                            <span>2002</span>
                        </div>
                        <div className="desc">
                            Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                            Necessitatibus laudantium, neque quia voluptates adipisci id
                            qui esse inventore at.
                        </div>
                        <div className="genre">Fiction</div>
                    </div>
                </>
            )}

        </div>
    )
}
