import React from 'react';

import Navbar from '../../components/Navbar/Navbar';
import './home.scss'
import Featured from '../../components/featured/Featured'
import List from '../../components/list/List';

const Home = () => {
    return (
        <div className='home'>
            <Navbar/>
            <Featured type=""/>
            <List/>
            <div style={{height:300}}></div>
        </div>
    )
}

export default Home
