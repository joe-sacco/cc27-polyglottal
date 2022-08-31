import { useEffect, useState } from "react";
import App from "./App";
import '../styles/Dropdown.css';

function Dropdown(props) {

    // useEffect(() => {
    // }, [])
    const scaleSelector = async () => {
        await props.setScale(document.querySelector('.scale-menu').value);
        console.log(props.scale);
    }

    return (
        <>
            <div className="dropdown-container">
                <h2 className="scales-lable">Pick a scale</h2>
                <select className="scale-menu" onChange={scaleSelector}>
                {/* scale setting inspired by https://www.windsongchimes.com.au/ */}
                    <option value="calm">Calm (pentatonic)</option>
                    <option value="reflective">Reflective (minor)</option>
                    <option value="hopeful">Hopeful (ancient)</option>
                </select>
            </div>
        </>
    );

}


export default Dropdown;