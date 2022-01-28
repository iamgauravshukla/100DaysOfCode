import React, { useState } from 'react'
import './navbar.scss'
import SearchIcon from '@mui/icons-material/Search';
import NotificationsIcon from '@mui/icons-material/Notifications';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';

const Navbar = () => {
    const [isScrolled, setIsScrolled] = useState(false);
    
    window.onscroll = () =>{
        setIsScrolled(window.pageYOffset === 0 ? false : true);
        return () => window.onscroll = null;
    };

    return (
        <div className={isScrolled ? 'navbar scrolled' : 'navbar'}>
            <div className="container">
                <div className="left">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" alt="" />
                    <span>Homepage</span>
                    <span>Series</span>
                    <span>Movies</span>
                    <span>New and Popular</span>
                    <span>My List</span>
                </div>

                <div className="right">
                    <SearchIcon className='icon'/>
                    <span>
                        KID
                    </span>
                    <NotificationsIcon className='icon'/>
                    <img src="https://scontent.fpat2-2.fna.fbcdn.net/v/t39.30808-6/258872358_2668059203338195_5343717544389818854_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=z9JAYNA11EQAX8hK7Q4&_nc_ht=scontent.fpat2-2.fna&oh=00_AT9NfHWzFw0uksUu-TWaCOAzovz72m6wRfq83QdOMiIM9A&oe=61F67FC3" alt="" />
                    <div className="profile">
                        <ArrowDropDownIcon className='icon'/>
                        <div className="options">
                            <span>Setting</span>
                            <span>Logout</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Navbar
