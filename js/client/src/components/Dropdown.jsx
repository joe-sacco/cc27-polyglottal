import '../styles/Dropdown.css';

function Dropdown(props) {
    const scaleSelector = async () => {
        await props.setScale(document.querySelector('.scale-menu').value);
    }

    return (
        <>
            <div className="dropdown-container">
                <h2 className="scales-lable">Pick a scale</h2>
                <select className="scale-menu" onChange={scaleSelector}>
                    <option value="calm">Calm (pentatonic)</option>
                    <option value="reflective">Reflective (minor)</option>
                    <option value="hopeful">Hopeful (ancient)</option>
                </select>
            </div>
        </>
    );
}

export default Dropdown;