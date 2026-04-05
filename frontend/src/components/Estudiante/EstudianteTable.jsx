import { useState, useEffect, useTransition } from "react";
import api from "../../config/api";

function EstudianteTable () {
    const [estudiantes, setEstudiantes] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [filtroAnioSeccion, setFiltroAnioSeccion] = useState('');
    const [anioSecciones, setAnioSecciones] = useState([]);

    useEffect(() => {
        fetchEstudiantes();
        fetchAniosSecciones();
    }, []);

    const fetchEstudiantes = async () => {
        try {
            setLoading(true)
            const params = filtroAnioSeccion ? {anio_seccion_id: filtroAnioSeccion} : {};
            const response = await api.get("/estudiante/", {params});
            setEstudiantes(response.data);
            setError(null);
        } catch (err) {
            console.error('Error al cargar los estudiantes:', err);
            setError('No se pudieron cargar los estudiantes');
        } finally {
            setLoading(false);
        }
    };

    const fetchAniosSecciones = async () => {
        try {
            const response = await api.get('/anio-seccion/');
            setAnioSecciones(response.data);
        } catch (err) {
            console.error('Error al cargar los anio y secciones', err);
        }
    };

    const estudiantesFiltrados = estudiantes.filter(est => {
        const nombreCompleto = `${est.primer_nom} ${est.segundo_nom || ''} ${est.primer_ape} ${est.segundo_ape}`.toLowerCase();
        const ciStr = String(est.ci);
        const busqueda = searchTerm.toLowerCase();
        return nombreCompleto.includes(busqueda) || ciStr.includes(busqueda);
    });

    if (loading) {
        return <div className="table-container"><div className="loading">⏳ Cargando estudiantes...</div></div>
    }

    if (error) {
        return (
            <div className="table-container">
                <div className="alert alert-error">{error}</div>
                <button onClick={fetchEstudiantes} className="btn-retry">🔄 Reintentar</button>
            </div>
        );
    }

    return (
        <div className="table-container">
            <div className="table-header">
                <h2>Lista de estudiantes</h2>
                <button onClick={fetchEstudiantes} className="btn-refresh">🔄 Actualizar</button>
            </div>

            {/* Filtros */}
            <div className="filters-bar">
                <div className="search-box">
                    <input 
                        type="text" 
                        placeholder="Buscar por nombre o numero de cedula"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </div>
                <div className="filter-box">
                    <select 
                        value={filtroAnioSeccion}
                        onChange={(e) => {
                            setFiltroAnioSeccion(e.target.value);
                            setTimeout(fetchEstudiantes, 100);
                        }}
                        >
                            <option value="">Todos los años / secciones</option>
                            {anioSecciones.map((as) => {
                                <option key={as.id} value={as.id}>
                                    {as.anio}° "{as.seccion}"
                                </option>
                            })}
                        </select>
                </div>
            </div>

            <div className="table-wrapper">
                <table className="data-table">
                    <thead>
                        <tr>
                            <th>CI</th>
                            <th>Nombre Completo</th>
                            <th>Año / Seccion</th>
                        </tr>
                    </thead>
                    <tbody>
                        {estudiantesFiltrados.length > 0 ? (
                            estudiantesFiltrados.map((est) => (
                                <tr key={est.ci}>
                                    <td className="ci-cell">{est.ci}</td>
                                    <td className="nombre-cell">
                                        {est.primer_nom} {est.segundo_nom || ''} {est.primer_ape} {est.segundo_ape}
                                    </td>
                                    <td className="anio-seccion-cell">
                                        {est.anio_seccion ? `${est.anio_seccion.anio}° "${est.anio_seccion.seccion}"` : 'Sin Asignar'}
                                    </td>
                                </tr>
                            ))
                        ): (
                            <tr>
                                <td colSpan={3} className="no-data">
                                    {searchTerm || filtroAnioSeccion ? 'No se encontraron resultados' : 'No hay estudiantes registrados'}
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>

            <div className="table-footer">
                <span>Total: <strong>{estudiantesFiltrados.length}</strong> de <strong>{estudiantes.length}</strong> estudiantes</span>
            </div>
        </div>
    );
}

export default EstudianteTable;