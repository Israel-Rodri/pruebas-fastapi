import { useState, useEffect, useTransition } from "react";
import api from "../../config/api"

function AnioSeccionTable () {
    //Estado para los datos
    const [registros, setRegistros] = useState([]);

    //Estados para la UI
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [deletingId, setDeletingId] = useState(null);

    useEffect(() => {
        fetchRegistros();
    }, []);

    const fetchRegistros = async () => {
        try {
            setLoading(true);
            const response = await api.get("/anio-seccion/");
            setRegistros(response.data);
            setError(null);
        } catch (err) {
            console.error("Error al cargar los datos", err);
            setError("No se pudieron cargar los datos del registro. Verfique que el backend se este ejecutando de forma correcta");
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (id) => {
        if (!window.confirm("¿Está seguro de eliminar este registro?")){
            return;
        } 
        try {
            setDeletingId(id);
            await api.delete(`/anio-seccion/${id}`);
            setRegistros(prev => prev.filter(reg => reg.id !== id));
            alert("Registro eliminado");
        } catch (err) {
            console.error("Error al eliminar", err);
            const msj = err.response?.data?.detail || "Error al eliminar el registro";
            alert(msj);
        } finally {
            setDeletingId(null);
        }
    };

    const registrosFiltrados = registros.filter(reg =>
        reg.anio.toLowerCase().includes(searchTerm.toLocaleLowerCase()) || 
        reg.seccion.toLowerCase().includes(searchTerm.toLowerCase())
    );

    if (loading) {
        return (
            <div className="table-container">
                <div className="loading">⏳ Cargando datos...</div>
            </div>
        );
    }

    if (error) {
        return(
            <div className="table-container">
                <div className="alert alert-error">{error}</div>
                <button onClick={fetchRegistros} className="btn-retry">🔄 Reintentar</button>
            </div>
        );
    }

    return(
        <div className="table-container">
            <div className="table-header">
                <h2>Años y secciones Registrados</h2>
                <button onClick={fetchRegistros} className="btn-refresh">🔄 Actualizar</button>
            </div>
            <div className="search-bar">
                <input 
                    type="text" 
                    placeholder="Buscar por año o seccion"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
            </div>
            <div className="table-wrapper">
                <table className="data-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Año</th>
                            <th>Sección</th>
                            <th>Código</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {registrosFiltrados.length > 0? (
                            registrosFiltrados.map((registro) => (
                                <tr key={registro.id}>
                                    <td>{registro.id}</td>
                                    <td className="anio-cell">{registro.anio}°</td>
                                    <td className="seccion-cell">{registro.seccion}</td>
                                    <td className="codigo-cell">{registro.anio}{registro.seccion}</td>
                                    <td>
                                        <button
                                            onClick={() => handleDelete(registro.id)}
                                            disabled={deletingId === registro.id}
                                            className="btn-delete"
                                        >
                                            {deletingId === registro.id ? '⏳' : '🗑️'}
                                        </button>
                                    </td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="5" className="no-data">
                                    {searchTerm ? 'No se encontraron resultados' : 'No hay registros disponibles'}
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>

            <div className="table-footer">
                <span>Total: <strong>{registrosFiltrados.length}</strong> de {registros.length} registros</span>
            </div>
        </div>
    );
}

export default AnioSeccionTable;