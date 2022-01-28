import React from 'react';
import Video from '../../files/Video.mov'
import './watch.scss'
import ArrowBackOutlinedIcon from '@mui/icons-material/ArrowBackOutlined';
export default function Watch() {
  return (
  <div className='watch'>
    <div className="back">
      <ArrowBackOutlinedIcon/>
      Home
    </div>
    <video  className='video' autoPlay muted loop progress controls src={Video}></video>
  </div>
  )
}
