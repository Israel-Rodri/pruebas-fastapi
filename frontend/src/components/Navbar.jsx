import { useState } from "react";

function Navbar ({seccionActiva, cambiarSeccion}) {
    const [menuAbierto, SetMenuAbierto] = useState(false);

    const menuItems = [
        {id: 'anio-seccion', label:'📚 Años y secciones', icon: '📚'},
        {id: 'estudiantes', label:'👨‍🎓 Estudiantes', icon: '👨‍🎓'},
        {id: 'notas', label:'📝 Notas', icon: '📝'}
    ];

    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <h1>Sistema Escolar</h1>
                <button className="menu-toggle" onClick={() => SetMenuAbierto(!menuAbierto)}>
                    ☰
                </button>
            </div>
            <ul className={`navbar-menu ${menuAbierto ? 'active': ''}`}>
                {menuItems.map((item) => (
                    <li key={item.id}>
                        <button
                            className={`nav-link ${seccionActiva === item.id ? 'active': ''}`}
                            onClick={() => {
                                if (!item.disabled) {
                                    cambiarSeccion(item.id);
                                    SetMenuAbierto(false);
                                }
                            }}
                            disabled={item.disabled}
                        >
                            <span className="nav-icon">{item.icon}</span>
                            <span className="nav-label">{item.label}</span>
                        </button>
                    </li>
                ))}
            </ul>
        </nav>
    );
}

export default Navbar;